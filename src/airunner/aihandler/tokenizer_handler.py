from transformers import AutoTokenizer, RagTokenizer

from airunner.aihandler.transformer_base_handler import TransformerBaseHandler


class TokenizerHandler(TransformerBaseHandler):
    tokenizer_class_ = AutoTokenizer

    @property
    def tokenizer_path(self):
        return self.current_model_path

    def post_load(self):
        self.load_tokenizer()

    def load_tokenizer(self, local_files_only=None):
        self.logger.info(f"Loading tokenizer from {self.current_model_path}")
        local_files_only = self.local_files_only if local_files_only is None else local_files_only
        chat_template = (
            "{{ bos_token }}"
            "{% for message in messages %}"
            "{% if message['role'] == 'system' %}"
            "{{ '[INST] <<SYS>>' + message['content'] + ' <</SYS>>[/INST]' }}"
            "{% elif message['role'] == 'user' %}"
            "{{ '[INST] ' + message['content'] + ' [/INST]' }}"
            "{% elif message['role'] == 'assistant' %}"
            "{{ message['content'] + eos_token + ' ' }}"
            "{% endif %}"
            "{% endfor %}"
        )
        try:
            self.tokenizer = self.tokenizer_class_.from_pretrained(
                self.tokenizer_path,
                local_files_only=local_files_only,
                token=self.request_data.get("hf_api_key_read_key"),
                device_map=self.device,
                chat_template=chat_template,
            )
            self.logger.info("Tokenizer loaded")
        except OSError as e:
            if "Checkout your internet connection" in str(e):
                if local_files_only:
                    self.logger.warning(
                        "Unable to load tokenizer, model does not exist locally, trying to load from remote"
                    )
                    return self.load_tokenizer(local_files_only=False)
                else:
                    self.logger.error(e)
        except Exception as e:
            self.logger.error(e)

        if self.tokenizer:
            self.tokenizer.use_default_system_prompt = False
        else:
            self.logger.error("Tokenizer failed to load")

class RAGTokenizerHandler(TokenizerHandler):
    tokenizer_class_ = RagTokenizer