from setuptools import setup, find_packages

setup(
    name='airunner',
    version="3.0.0.dev1",
    author="Capsize LLC",
    description="A Stable Diffusion GUI",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    keywords="ai, stable diffusion, art, ai art, stablediffusion",
    license="AGPL-3.0",
    author_email="contact@capsizegames.com",
    url="https://github.com/Capsize-Games/airunner",
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires=">=3.10.0",
    install_requires=[
        "einops==0.7.0",
        "ninja==1.11.1.1",
        "JIT==0.2.7",
        "tqdm==4.66.2",
        "omegaconf==2.3.0",
        "accelerate==0.28.0",
        "controlnet_aux==0.0.7",
        "diffusers==0.27.0",
        "huggingface-hub==0.21.4",
        "numpy==1.26.4",
        "Pillow==10.2.0",
        "pip==24.0",
        "PySide6==6.6.2",
        "PySide6_Addons==6.6.2",
        "PySide6_Essentials==6.6.2",
        "pyre-extensions==0.0.30",
        "lightning==2.2.1",
        "requests==2.31.0",
        "requests-oauthlib==2.0.0",
        "safetensors==0.4.2",
        "scipy==1.12.0",
        "tokenizers==0.15.2",
        "tqdm==4.66.2",
        "charset-normalizer==3.3.2",
        "opencv-python-headless==4.9.0.80",
        "setuptools==69.2.0",
        "typing_extensions==4.10.0",
        "urllib3==2.2.1",
        "transformers==4.38.2",
        "compel==2.0.2",
        "sympy==1.12.0",
        "regex",
        "matplotlib==3.8.3",
        "torch==2.2.1",
        "torchvision==0.17.1",
        "torchaudio==2.2.1",
        "auto-gptq==0.7.1",
        "optimum==1.17.1",
        "bitsandbytes==0.43.0",
        "tomesd==0.1.3",
        "watchdog==4.0.0",
        "sounddevice==0.4.6",
        "datasets==2.18.0",
        "sentence_transformers==2.5.1",
        "inflect==7.0.0",
        "tiktoken==0.6.0",
        "pycountry==23.12.11",
        "pyttsx3==2.90",
        "mediapipe==0.10.11",
        "coverage==7.4.4"
    ],
    dependency_links=[]
)
