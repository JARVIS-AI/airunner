from airunner.aihandler.stt_handler import STTHandler
from airunner.workers.worker import Worker


class AudioProcessorWorker(Worker):
    """
    This class is responsible for processing audio.
    It will process audio from the audio_queue and send it to the model.
    """ 
    fs = 0

    def __init__(self, prefix):
        super().__init__(prefix=prefix)
        self.stt = STTHandler()
        self.register("stt_audio_processed", self)
    
    def on_stt_audio_processed(self, transcription):
        self.emit("response_signal", transcription)

    def handle_message(self, audio_data):
        self.emit("processed_audio", audio_data)
    
    def update_properties(self):
        settings = self.application_settings.value("settings")
        self.fs = settings["stt_settings"]["fs"]