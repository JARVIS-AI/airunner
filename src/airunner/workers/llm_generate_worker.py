from airunner.workers.worker import Worker
from airunner.aihandler.llm_handler import LLMHandler


class LLMGenerateWorker(Worker):
    def __init__(self, prefix="LLMGenerateWorker"):
        self.llm = LLMHandler()
        super().__init__(prefix=prefix)
        self.register("clear_history", self)
        self.register("LLMRequestWorker_response_signal", self)
        self.register("unload_llm_signal", self)

    def on_unload_llm_signal(self, message):
        """
        This function will either 
        
        1. Leave the LLM on the GPU
        2. Move it to the CPU
        3. Unload it from memory

        The choice is dependent on the current dtype and other settings.
        """
        do_unload_model = message.get("do_unload_model", False)
        move_unused_model_to_cpu = message.get("move_unused_model_to_cpu", False)
        do_move_to_cpu = not do_unload_model and move_unused_model_to_cpu
        dtype = message.get("dtype", "")
        callback = message.get("callback", None)
        if dtype in ["2bit", "4bit", "8bit"]:
            do_unload_model = True
            do_move_to_cpu = False
        if do_move_to_cpu:
            self.logger.info("Moving LLM to CPU")
            self.llm.move_to_cpu()
        elif do_unload_model:
            self.llm.unload()
        if callback:
            callback()

    def on_LLMRequestWorker_response_signal(self, message):
        self.add_to_queue(message)

    def handle_message(self, message):
        for response in self.llm.do_generate(message):
            self.emit("llm_text_streamed_signal", response)
    
    def on_clear_history(self):
        self.llm.clear_history()
    
    def unload_llm(self):
        self.llm.unload()