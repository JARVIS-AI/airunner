"""
A class which builds the UI for the application.

This is a stand alone function which:

1. iterates recursively over pyqt/templates and pyqt/widgets *.ui files
2. runs `pyuic6 -o <file_name>.py <file_name>.ui` on each *.ui file
3. runs `pyside6-rcc -o resources.py resources.qrc`

The function will run using the venv python interpreter
"""
import os
import re
import subprocess
from pathlib import Path

from airunner.utils import get_venv_python_executable


def adjust_resource_imports(input_file, output_file):
    # Define the pattern to find the original import lines
    pattern = re.compile(r'^import (.+_rc)$', re.MULTILINE)
    # Define the replacement string, incorporating your namespace
    replacement = r'import airunner.\1'

    with open(input_file, 'r') as file:
        content = file.read()

    # Replace the import statements with the ones including your namespace
    adjusted_content = re.sub(pattern, replacement, content)

    with open(output_file, 'w') as file:
        file.write(adjusted_content)


def build_ui(path):
    """Build the UI for the application."""
    print("Building UI at path", path)
    ui_files = Path(__file__).parent.parent.joinpath(path).glob("**/*.ui")
    for ui_file in ui_files:

        print("Generating", ui_file)
        ui_file = str(ui_file)
        ui_file_dir = os.path.dirname(ui_file)
        ui_file_py = ui_file.replace(".ui", "_ui.py")
        print(f"Generating {ui_file_py}")
        subprocess.run(
            [
                "pyside6-uic",
                "-o",
                ui_file_py,
                ui_file,
            ],
            cwd=ui_file_dir,
        )

        adjust_resource_imports(ui_file_py, ui_file_py)

def generate_resources():
    print("Generating resources.py")
    subprocess.run(
        [
            "pyside6-rcc",
            "-o",
            "src/airunner/resources_light_rc.py",
            "src/airunner/resources_light.qrc",
        ],
        cwd=str(Path(__file__).parent.parent),
    )
    subprocess.run(
        [
            "pyside6-rcc",
            "-o",
            "src/airunner/resources_dark_rc.py",
            "src/airunner/resources_dark.qrc",
        ],
        cwd=str(Path(__file__).parent.parent),
    )


if __name__ == "__main__":
    for dir in ["widgets", "windows"]:
        path = os.path.join("src", "airunner", dir)
        build_ui(path)
    generate_resources()