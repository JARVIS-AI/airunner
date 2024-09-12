import queue

from PySide6.QtCore import QObject, Signal, Slot

from airunner.enums import QueueType, SignalCode, ModelType, ModelStatus
from airunner.settings import AVAILABLE_DTYPES, SLEEP_TIME_IN_MS
from airunner.workers.worker import Worker
from PySide6.QtCore import QThread


class LLMLoaderWorker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, llm, message):
        super().__init__()
        self.llm = llm
        self.message = message

    @Slot()
    def run(self):
        try:
            self.llm.on_load_llm_signal(self.message)
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()


class LLMGenerateWorker(Worker):
    def __init__(self, prefix=None, do_load_on_init=False, agent_class=None, agent_options=None):
        self.signals = [
            (SignalCode.LLM_UNLOAD_SIGNAL, self.on_unload_llm_signal),
            (SignalCode.LLM_LOAD_SIGNAL, self.on_load_llm_signal),
            (SignalCode.LLM_LOAD_MODEL_SIGNAL, self.on_load_model_signal),
            (SignalCode.LLM_CLEAR_HISTORY_SIGNAL, self.on_clear_history_signal),
            (SignalCode.INTERRUPT_PROCESS_SIGNAL, self.on_interrupt_process_signal),
            (SignalCode.RAG_RELOAD_INDEX_SIGNAL, self.on_reload_rag_index_signal),
        ]
        self.thread = None
        self.llm = None
        self.do_load_on_init = do_load_on_init
        self.agent_class = agent_class
        self.agent_options = agent_options
        super().__init__(prefix=prefix)
        self.llm_generate_worker = None
        self.thread = QThread()
        self.llm_generate_worker = LLMLoaderWorker(self.llm, "")
        self.llm_generate_worker.moveToThread(self.thread)

        self.thread.started.connect(self.llm_generate_worker.run)
        self.llm_generate_worker.finished.connect(self.thread.quit)
        self.llm_generate_worker.finished.connect(self.llm_generate_worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.llm_generate_worker.error.connect(self.handle_error)

    def on_reload_rag_index_signal(self, data: dict = None):
        self.llm.chat_agent.reload_rag(data)

    def on_unload_llm_signal(self, message):
        if self.thread.isRunning():
            self.stop_thread()
        if self.llm:
            self.llm.on_unload_llm_signal(message)

    def stop_thread(self):
        self.thread.quit()
        self.thread.wait()
        self.thread = None

    def on_load_llm_signal(self, message: dict):
        if self.thread is not None:
            return
        self.emit_signal(
            SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                "model": ModelType.LLM,
                "status": ModelStatus.LOADING,
                "path": ""
            }
        )
        self.llm_generate_worker.message = message
        self.thread.start()

    def handle_error(self, error_message):
        print(f"Error: {error_message}")

    def on_load_model_signal(self):
        if self.llm:
            self.llm.on_load_model_signal()

    def on_clear_history_signal(self):
        if self.llm:
            self.llm.on_clear_history_signal()

    def on_interrupt_process_signal(self):
        if self.llm:
            self.llm.on_interrupt_process_signal()

    def start_worker_thread(self):
        from airunner.aihandler.llm.causal_lm_transfformer_base_handler import CausalLMTransformerBaseHandler

        if self.settings["llm_enabled"]:
            self.emit_signal(
                SignalCode.MODEL_STATUS_CHANGED_SIGNAL, {
                    "model": ModelType.LLM,
                    "status": ModelStatus.LOADING,
                    "path": ""
                }
            )
        self.llm = CausalLMTransformerBaseHandler(
            do_load_on_init=self.do_load_on_init,
            agent_class=self.agent_class,
            agent_options=self.agent_options
        )

    # def start(self):
    #     try:
    #         loop = asyncio.get_event_loop()
    #     except RuntimeError:
    #         loop = asyncio.new_event_loop()
    #
    #     if loop.is_running():
    #         loop.create_task(self.start_consuming())
    #     else:
    #         asyncio.run(self.start_consuming())

    def on_unload_llm_signal(self, message: dict):
        """
        This function will either 
        
        1. Leave the LLM on the GPU
        2. Move it to the CPU
        3. Unload it from memory

        The choice is dependent on the current dtype and other settings.
        """
        settings = self.settings
        dtype = settings["llm_generator_settings"]["dtype"]
        do_unload_model = settings["memory_settings"]["unload_unused_models"]
        move_unused_model_to_cpu = settings["memory_settings"]["move_unused_model_to_cpu"]
        do_move_to_cpu = not do_unload_model and move_unused_model_to_cpu
        callback = message.get("callback", None)
        if dtype in AVAILABLE_DTYPES:
            do_unload_model = True
            do_move_to_cpu = False
        if do_move_to_cpu:
            self.logger.debug("Moving LLM to CPU")
            self.llm.move_to_cpu()
        elif do_unload_model:
            self.unload_llm()
        if callback:
            callback()

    def run(self):
        if self.queue_type == QueueType.NONE:
            return
        self.logger.debug("Starting LLM generate worker")
        self.running = True
        while self.running:
            self.preprocess()
            try:
                msg = self.get_item_from_queue()
                if msg is not None:
                    self.handle_message(msg)
            except queue.Empty:
                msg = None
            if self.paused:
                self.logger.debug("Paused")
                while self.paused:
                    QThread.msleep(SLEEP_TIME_IN_MS)
                self.logger.debug("Resumed")
            QThread.msleep(SLEEP_TIME_IN_MS)

    def llm_load_signal(self, data: dict):
        print("llm_load_signal called from nats with", data)

    def on_llm_request_worker_response_signal(self, message: dict):
        self.add_to_queue(message)

    def handle_message(self, message):
        if self.llm:
            # try:
            self.llm.handle_request(message)
            # except Exception as e:
            #     self.logger.error(f"Error in handle_message: {e}")
            #     self.logger.error(f"Message: {message}")

    def unload_llm(self):
        self.logger.debug("Unloading LLM")
        if self.llm:
            self.llm.unload()
