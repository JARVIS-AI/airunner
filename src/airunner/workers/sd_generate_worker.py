import os
import torch

from airunner.aihandler.enums import EngineResponseCode
from airunner.workers.worker import Worker
from airunner.aihandler.runner import SDRunner

torch.backends.cuda.matmul.allow_tf32 = True


class SDGenerateWorker(Worker):
    def __init__(self, prefix="SDGenerateWorker"):
        super().__init__(prefix=prefix)
        self.sd = SDRunner()
        self.register("add_sd_response_to_queue_signal", self)
    
    def on_add_sd_response_to_queue_signal(self, request):
        self.logger.info("Request recieved")
        self.add_to_queue(request)
        
    def handle_message(self, data):
        self.logger.info("Generating")
        image_base_path = data["image_base_path"]
        message = data["message"]
        for response in self.sd.generator_sample(message):
            print("RESPONSE FROM sd.generate_sample", response)
            if not response:
                continue

            images = response['images']
            data = response["data"]
            nsfw_content_detected = response["nsfw_content_detected"]
            if nsfw_content_detected:
                self.emit("nsfw_content_detected_signal", response)
                continue

            seed = data["options"]["seed"]
            updated_images = []
            for index, image in enumerate(images):
                # hash the prompt and negative prompt along with the action
                action = data["action"]
                prompt = data["options"]["prompt"][0]
                negative_prompt = data["options"]["negative_prompt"][0]
                prompt_hash = hash(f"{action}{prompt}{negative_prompt}{index}")
                image_name = f"{prompt_hash}_{seed}.png"
                image_path = os.path.join(image_base_path, image_name)
                # save the image
                image.save(image_path)
                updated_images.append(dict(
                    path=image_path,
                    image=image
                ))
            response["images"] = updated_images
            self.emit("engine_do_response_signal", dict(
                code=EngineResponseCode.IMAGE_GENERATED,
                message=response
            ))