#!/usr/bin/env python
"""
----------------------------------------------------------------
Import order is crucial for AI Runner to work as expected.
Do not remove the no_internet_socket import.
Do not change the order of the imports.
----------------------------------------------------------------
"""
################################################################
# Importing this module sets the Hugging Face environment
# variables for the application.
################################################################
# import facehuggershield
# facehuggershield.huggingface.activate(
#     show_stdout=True,
#     darklock_os_whitelisted_directories=["~/.airunner", "/tmp"]
# )
import os
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"

################################################################
# Import the main application class for AI Runner.
################################################################
from airunner.app import App

################################################################
# Import Alembic modules to run migrations.
################################################################
from alembic.config import Config
from alembic import command

def run_alembic_upgrade():
    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")

if __name__ == "__main__":
    run_alembic_upgrade()
    App(
        restrict_os_access=None,
        #defendatron=facehuggershield.huggingface.defendatron
    )
