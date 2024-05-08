SD_FILE_BOOTSTRAP_DATA = {
    "SD 1.5": {
        "txt2img": [
            "feature_extractor/preprocessor_config.json",
            "safety_checker/config.json",
            "safety_checker/model.safetensors",
            "scheduler/scheduler_config.json",
            "text_encoder/config.json",
            "text_encoder/model.safetensors",
            "tokenizer/merges.txt",
            "tokenizer/special_tokens_map.json",
            "tokenizer/tokenizer_config.json",
            "tokenizer/vocab.json",
            "unet/config.json",
            "unet/diffusion_pytorch_model.safetensors",
            "v1-inference.yaml",
            "vae/config.json",
            "vae/diffusion_pytorch_model.safetensors",
            "model_index.json",
            "v1-5-pruned-emaonly.safetensors",
            "v1-inference.yaml",
        ],
        "datasets": [
            "Matthijs/cmu-arctic-xvectors"
        ],
        "safety_checker": [
            "config.json",
            "preprocessor_config.json",
            "pytorch_model.bin"
        ],
        "feature_extractor": [
            "config.json",
            "model.safetensors",
            "preprocessor_config.json",
            "special_tokens_map.json",
            "tokenizer.json",
            "tokenizer_config.json",
            "vocab.json"
        ],
        "inpaint": [
            "feature_extractor/preprocessor_config.json",
            "safety_checker/config.json",
            "safety_checker/model.safetensors",
            "scheduler/scheduler_config.json",
            "text_encoder/config.json",
            "text_encoder/model.safetensors",
            "tokenizer/merges.txt",
            "tokenizer/special_tokens_map.json",
            "tokenizer/tokenizer_config.json",
            "tokenizer/vocab.json",
            "unet/config.json",
            "unet/diffusion_pytorch_model.safetensors",
            "vae/config.json",
            "vae/diffusion_pytorch_model.safetensors",
            "config.json",
            "model_index.json",
            "sd-v1-5-inpainting.ckpt"
        ],
        "depth2img": [
            "depth_estimator/config.json",
            "depth_estimator/model.safetensors",
            "feature_extractor/preprocessor_config.json",
            "scheduler/scheduler_config.json",
            "text_encoder/config.json",
            "text_encoder/model.safetensors",
            "tokenizer/merges.txt",
            "tokenizer/special_tokens_map.json",
            "tokenizer/tokenizer_config.json",
            "tokenizer/vocab.json",
            "unet/config.json",
            "unet/diffusion_pytorch_model.safetensors",
            "vae/config.json",
            "vae/diffusion_pytorch_model.safetensors",
            "512-depth-ema.safetensors",
            "model_index.json",
        ],
        "controlnet": [
            "config.json",
            "diffusion_pytorch_model.safetensors",
        ],
        # "superresolution": [
        #     "low_res_scheduler/scheduler_config.json",
        #     "scheduler/scheduler_config.json",
        #     "text_encoder/config.json",
        #     "text_encoder/model.safetensors",
        #     "tokenizer/merges.txt",
        #     "tokenizer/special_tokens_map.json",
        #     "tokenizer/tokenizer_config.json",
        #     "tokenizer/vocab.json",
        #     "unet/config.json",
        #     "unet/diffusion_pytorch_model.safetensors",
        #     "vae/config.json",
        #     "vae/diffusion_pytorch_model.safetensors",
        #     "model_index.json",
        #     "x4-upscaler-ema.safetensors",
        # ],
        "pix2pix": [
            "feature_extractor/preprocessor_config.json",
            "safety_checker/config.json",
            "safety_checker/model.safetensors",
            "scheduler/scheduler_config.json",
            "text_encoder/config.json",
            "text_encoder/model.safetensors",
            "tokenizer/merges.txt",
            "tokenizer/special_tokens_map.json",
            "tokenizer/tokenizer_config.json",
            "tokenizer/vocab.json",
            "unet/config.json",
            "unet/diffusion_pytorch_model.safetensors",
            "vae/config.json",
            "vae/diffusion_pytorch_model.safetensors",
            "model_index.json",
            "instruct-pix2pix-00-22000.safetensors",
        ],
        # "upscale": [
        #     "scheduler/scheduler_config.json",
        #     "text_encoder/config.json",
        #     "text_encoder/model.safetensors",
        #     "text_encoder/pytorch_model.bin",
        #     "tokenizer/merges.txt",
        #     "tokenizer/special_tokens_map.json",
        #     "tokenizer/tokenizer_config.json",
        #     "tokenizer/vocab.json",
        #     "unet/config.json",
        #     "unet/diffusion_pytorch_model.safetensors",
        #     "vae/config.json",
        #     "vae/diffusion_pytorch_model.safetensors",
        #     "model_index.json",
        # ]
    }
}