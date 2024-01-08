import torch
import random

from PyQt6.QtCore import QObject

# import AutoTokenizer
# import BitsAndBytesConfig
from transformers import BitsAndBytesConfig
from transformers import AutoModelForCausalLM, AutoModelForSeq2SeqLM, AutoTokenizer
from transformers import InstructBlipForConditionalGeneration
from transformers import InstructBlipProcessor

from airunner.aihandler.settings_manager import SettingsManager
from airunner.data.models import LLMGenerator
from airunner.data.db import session
from airunner.aihandler.logger import Logger


class TransformerRunner(QObject):
    dtype = ""
    local_files_only = True
    set_attention_mask = False
    do_push_to_hub = False
    llm_int8_enable_fp32_cpu_offload = True
    use_gpu = True
    generator_name = ""
    model_path = ""
    default_model_path = ""
    current_model_path = ""
    request_type = ""
    top_k = 20
    eta_cutoff = 10
    top_p = 1.0
    num_beams = 1
    repetition_penalty = 100.0
    early_stopping = True
    max_length = 200
    min_length = 0
    temperature = 1.0
    return_result = True
    skip_special_tokens = True
    override_parameters = False
    model = None
    processor = None
    do_sample = True
    _processing_request = False
    bad_words_ids=None
    bos_token_id=None
    pad_token_id=None
    eos_token_id=None
    no_repeat_ngram_size=1
    sequences=1
    decoder_start_token_id=None
    use_cache=False
    seed=42
    tokenizer = None
    _generator = None
    requested_generator_name = ""
    current_generator_name = ""
    do_quantize_model = True
    callback = None
    template = None
    #system_instructions = ""
    system_instructions = ""

    @property
    def generator(self):
        try:
            if not self._generator or self.current_generator_name != self.requested_generator_name:
                self.current_generator_name = self.requested_generator_name
                self._generator = session.query(LLMGenerator).filter_by(name=self.current_generator_name).first()
            return self._generator
        except Exception as e:
            Logger.error(e)
    
    @property
    def do_load_model(self):
        if self.model is None or self.current_model_path != self.model_path:
            return True
        return False

    @property
    def device_map(self):
        return "cpu" if not self.has_gpu else "auto"

    @property
    def has_gpu(self):
        if self.dtype == "32bit" or not self.use_gpu:
            return False
        return torch.cuda.is_available()

    def __init__(self, *args, **kwargs):
        self.engine = kwargs.pop("engine", None)
        app = kwargs.pop("app", None)
        self.app = app
        super().__init__(*args, **kwargs)
        self.settings_manager = SettingsManager()
        # self.llm_api = LLMAPI(app=app)

    def move_to_cpu(self):
        if self.model:
            Logger.info("Moving model to CPU")
            self.model.to("cpu")
        self.tokenizer = None

    def move_to_device(self, device=None):
        if not self.model:
            return
        if device:
            device_name = device
        elif self.dtype in ["2bit", "4bit", "8bit", "16bit"] and self.has_gpu:
            device_name = "cuda"
        else:
            device_name = "cpu"
        Logger.info("Moving model to device {device_name}")
        self.model.to(device_name)
    
    def unload_tokenizer(self):
        Logger.info("Unloading tokenizer")
        self.tokenizer = None
        self.engine.clear_memory()
        
    def unload_model(self):
        self.model = None
        self.processor = None
        self.engine.clear_memory()

    def quantization_config(self):
        config = None
        if self.dtype == "8bit":
            Logger.info("Loading 8bit model")
            config = BitsAndBytesConfig(
                load_in_4bit=False,
                load_in_8bit=True,
                llm_int8_threshold=200.0,
                llm_int8_has_fp16_weight=False,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type='nf4',
            )
        elif self.dtype == "4bit":
            Logger.info("Loading 4bit model")
            config = BitsAndBytesConfig(
                load_in_4bit=True,
                load_in_8bit=False,
                llm_int8_threshold=200.0,
                llm_int8_has_fp16_weight=False,
                bnb_4bit_compute_dtype=torch.float16,
                bnb_4bit_use_double_quant=True,
                bnb_4bit_quant_type='nf4',
            )
        return config

    def unload_processor(self):
        Logger.info("Unloading processor")
        self.processor = None
        self.engine.clear_memory()

    def load_processor(self, local_files_only = None):
        Logger.info(f"Loading processor {self.model_path}")
        local_files_only = self.local_files_only if local_files_only is None else local_files_only
        kwargs = {}
        config = self.quantization_config()
        if config:
            kwargs["quantization_config"] = config
        self.processor = InstructBlipProcessor.from_pretrained(
            self.model_path, 
            device_map="auto",
            torch_dtype=torch.float16,
            **kwargs
        )
        if self.processor:
            Logger.info("Processor loaded")
        else:
            Logger.error("Failed to load processor")

    def load_model(self, local_files_only = None):
        Logger.info("Loading model")
        if not self.do_load_model:
            return

        local_files_only = self.local_files_only if local_files_only is None else local_files_only

        params = {
            "local_files_only": local_files_only,
            "device_map": self.device_map,
            "use_cache": self.use_cache,
            "torch_dtype": torch.float16 if self.dtype != "32bit" else torch.float32,
            "token": self.settings_manager.hf_api_key_read_key,
            "trust_remote_code": True
        }
        
        if self.do_quantize_model:
            config = self.quantization_config()
            if config:
                params["quantization_config"] = config

        path = self.current_model_path
        #self.engine.send_message(f"Loading {self.generator.name} model from {path}")
        
        auto_class_ = None
        if self.generator.name == "seq2seq":
            auto_class_ = AutoModelForSeq2SeqLM
        elif self.generator.name == "casuallm":
            auto_class_ = AutoModelForCausalLM
        elif self.generator.name == "visualqa":
            auto_class_ = InstructBlipForConditionalGeneration
            params.pop("use_cache", None)
        
        Logger.info(f"Loading model from {path}")
        try:
            self.model = auto_class_.from_pretrained(path, **params)
        except OSError as e:
            if "Checkout your internet connection" in str(e):
                if local_files_only:
                    return self.load_model(local_files_only=False)
                else:
                    Logger.error(e)
        
        # if self.generator.name == "casuallm":
        #     self.pipeline = AutoModelForCausalLM.from_pretrained(
        #         self.model,
        #         torch_dtype=torch.float16 if self.dtype != "32bit" else torch.float32,
        #         trust_remote_code=False,
        #         device_map="auto"
        #     )

            
    def process_data(self, data):
        self.request_data = data.get("request_data", {})
        self.callback = self.request_data.get("callback", None)
        self.parameters = self.request_data.get("parameters", {})
        self.dtype = self.request_data.get("dtype", self.dtype)
        self.use_gpu = self.request_data.get("use_gpu", self.use_gpu)
        self.requested_generator_name = self.request_data.get("generator_name", self.generator_name)
        self.model_path = self.request_data.get("model_path", self.model_path)
        self.override_parameters = self.parameters.get("override_parameters", self.override_parameters)
        self.username = self.request_data.get("username", "")
        self.botname = self.request_data.get("botname", "")
        self.prompt = self.request_data.get("prompt", "")
        self.prompt_template = self.request_data.get("prompt_template", "")
        self.image = self.request_data.get("image", None)
        self.system_instructions = f"Your name is {self.botname}. You are talking to {self.username}. You will always respond in character. You will always respond to the user. You will not give ethical or moral advice to the user unless it is something appropriate for {self.botname} to say."
        if self.image:
            self.image = self.image.convert("RGB")
        
    def do_generate(self, data):
        self.process_data(data)
        self.handle_request()
    
    def handle_request(self):
        default_ = self.handle_generate_request
        {
            "clear_conversation": self.clear_conversation,
            "generate": default_,
        }.get(self.request_type, default_)()
    
    def clear_conversation(self):
        pass

    def prepare_input_args(self):
        self.system_instructions = self.request_data.get("system_instructions", "")
        top_k = self.parameters.get("top_k", self.top_k)
        eta_cutoff = self.parameters.get("eta_cutoff", self.eta_cutoff)
        top_p = self.parameters.get("top_p", self.top_p)
        num_beams = self.parameters.get("num_beams", self.num_beams)
        repetition_penalty = self.parameters.get("repetition_penalty", self.repetition_penalty)
        early_stopping = self.parameters.get("early_stopping", self.early_stopping)
        max_length = self.parameters.get("max_length", self.max_length)
        min_length = self.parameters.get("min_length", self.min_length)
        temperature = self.parameters.get("temperature", self.temperature)
        return_result = self.parameters.get("return_result", self.return_result)
        skip_special_tokens = self.parameters.get("skip_special_tokens", self.skip_special_tokens)
        do_sample = self.parameters.get("do_sample", self.do_sample)
        bad_words_ids = self.parameters.get("bad_words_ids", self.bad_words_ids)
        bos_token_id = self.parameters.get("bos_token_id", self.bos_token_id)
        pad_token_id = self.parameters.get("pad_token_id", self.pad_token_id)
        eos_token_id = self.parameters.get("eos_token_id", self.eos_token_id)
        no_repeat_ngram_size = self.parameters.get("no_repeat_ngram_size", self.no_repeat_ngram_size)
        sequences = self.parameters.get("sequences", self.sequences)
        decoder_start_token_id = self.parameters.get("decoder_start_token_id", self.decoder_start_token_id)
        use_cache = self.parameters.get("use_cache", self.use_cache)
        seed = self.parameters.get("seed", self.seed)
            
        kwargs = {
            "max_length": max_length,
            "min_length": min_length,
            "do_sample": do_sample,
            "early_stopping": early_stopping,
            "num_beams": num_beams,
            "temperature": temperature,
            "top_k": top_k,
            "eta_cutoff": eta_cutoff,
            "top_p": top_p,
            "repetition_penalty": repetition_penalty,
            # "bad_words_ids": bad_words_ids,
            # "bos_token_id": bos_token_id,
            # "pad_token_id": pad_token_id,
            # "eos_token_id": eos_token_id,
            "return_result": return_result,
            "skip_special_tokens": skip_special_tokens,
            "no_repeat_ngram_size": no_repeat_ngram_size,
            "num_return_sequences": sequences, # if num_beams == 1 or num_beams < sequences else num_beams,
            "decoder_start_token_id": decoder_start_token_id,
            "use_cache": use_cache,
            "seed": seed,
        }
        if "top_k" in kwargs and "do_sample" in kwargs and not kwargs["do_sample"]:
            del kwargs["top_k"]

        if self.generator.name == "visualqa":
            for key in ["return_result", "skip_special_tokens", "seed"]:
                kwargs.pop(key)
        

        return kwargs
    
    def load_tokenizer(self, local_files_only = None):
        if self.generator.name == "casuallm":
            local_files_only = self.local_files_only if local_files_only is None else local_files_only
            if not self.tokenizer is None:
                return
            Logger.info("Load tokenizer")
            try:
                self.tokenizer = AutoTokenizer.from_pretrained(
                    self.current_model_path,
                    local_files_only=local_files_only,
                    token=self.settings_manager.hf_api_key_read_key,
                    device_map=self.device_map,
                )
            except OSError as e:
                if "Checkout your internet connection" in str(e):
                    if local_files_only:
                        Logger.info("Unable to load tokenizer, model does not exist locally, trying to load from remote")
                        return self.load_tokenizer(local_files_only=False)
                    else:
                        Logger.error(e)
            if self.tokenizer:
                self.tokenizer.use_default_system_prompt = False

    def do_set_seed(self, seed=None):
        seed = self.seed if seed is None else seed
        self.seed = seed
        # _set_seed(self.seed)
        # set model and token seed
        torch.manual_seed(self.seed)
        torch.cuda.manual_seed(self.seed)
        torch.cuda.manual_seed_all(self.seed)
        random.seed(self.seed)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
        if self.tokenizer:
            self.tokenizer.seed = self.seed

    def handle_generate_request(self):
        self.disable_request_processing()
        kwargs = self.prepare_input_args()
        self.do_set_seed(kwargs.get("seed"))
        # Logger.info("Generating output")

        self.current_model_path = self.model_path
        self.load_tokenizer()
        self.load_model()
        if self.generator.name == "visualqa":
            self.load_processor()

        # self.engine.send_message("Generating output")
        # with torch.backends.cuda.sdp_kernel(
        #     enable_flash=True, 
        #     enable_math=False, 
        #     enable_mem_efficient=False
        # ):
        #     with torch.no_grad():
        #         print("************** CALLING GENERATE")
        #         value = self.generate()
        #         print("VALUE", value)
        #         # if self.callback:
        #         #     self.callback(value)
        #         # else:
        #         #     self.engine.send_message(value, code=MessageCode.TEXT_GENERATED)
        self.enable_request_processing()
    
    def disable_request_processing(self):
        self._processing_request = True
    
    def enable_request_processing(self):
        self._processing_request = True
    
    def generate(self):
        pass


    