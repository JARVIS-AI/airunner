"""
A class which builds the UI for the application.

This is a stand alone function which:

1. iterates recursively over pyqt/templates and pyqt/widgets *.ui files
2. runs `pyuic6 -o <file_name>.py <file_name>.ui` on each *.ui file
3. runs `pyside6-rcc -o resources.py resources.qrc`

The function will run using the venv python interpreter
"""
import os
import subprocess
from pathlib import Path

from airunner.utils import get_venv_python_executable


def build_ui(path):
    """Build the UI for the application."""
    # venv_python = get_venv_python_executable()
    # recursively iterate over directories in path
    print("Building UI at path", path)
    ui_files = Path(__file__).parent.parent.joinpath(path).glob("**/*.ui")
    for ui_file in ui_files:

        print("Generating", ui_file)
        ui_file = str(ui_file)
        ui_file_name = os.path.basename(ui_file)
        ui_file_dir = os.path.dirname(ui_file)
        ui_file_py = ui_file.replace(".ui", ".py")
        print(f"Generating {ui_file_py}")
        subprocess.run(
            [
                "pyuic6",
                "-o",
                ui_file_py,
                ui_file,
            ],
            cwd=ui_file_dir,
        )

def generate_resources():
    print("Generating resources.py")
    subprocess.run(
        [
            "pyside6-rcc",
            "-o",
            "resources.py",
            "resources.qrc",
        ],
        cwd=str(Path(__file__).parent.parent),
    )


if __name__ == "__main__":
    for dir in ["templates", "widgets", "windows"]:
        path = os.path.join("pyqt", dir)
        build_ui(path)
    generate_resources()
