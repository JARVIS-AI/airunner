from setuptools import setup, find_packages

setup(
    name='airunner',
    version="2.3.0",
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
        "tqdm==4.65.0",
        "omegaconf==2.3.0",
        "accelerate==0.23.0",
        "controlnet_aux==0.0.7",
        "diffusers==0.25.1",
        "huggingface-hub==0.20.2",
        "numpy==1.26.3",
        "Pillow==10.2.0",
        "pip==23.3.1",
        "PyQt6==6.6.1",
        "PyQt6-Qt6==6.4.2",
        "PyQt6-sip==13.6.0",
        "PySide6==6.4.2",
        "pyre-extensions==0.0.29",
        "lightning==2.0.2",
        "requests==2.31.0",
        "requests-oauthlib==1.3.1",
        "safetensors==0.3.1",
        "scipy==1.10.1",
        "tokenizers==0.15.0",
        "tqdm==4.65.0",
        "charset-normalizer==3.3.2",
        "opencv-python==4.9.0.80",
        "setuptools==67.7.2",
        "typing_extensions==4.9.0",
        "urllib3==2.1.0",
        "transformers==4.37.1",
        "compel==2.0.2",
        "sympy==1.12.0",
        "regex",
        "matplotlib==3.7.2",
        "torch==2.1.2",
        "torchvision==0.16.2",
        "torchaudio==2.1.2",
        "auto-gptq==0.6.0",
        "optimum==1.16.2",
        "bitsandbytes==0.42.0",
        "langchain==0.0.331",
        "tomesd==0.1.3"
    ],
    dependency_links=[]
)
