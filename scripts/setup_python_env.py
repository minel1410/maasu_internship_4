import subprocess
import shutil
import sys
from pathlib import Path


def is_venv(dir_path):
    dir_path = Path(dir_path)
    return dir_path.is_dir() and (
        (dir_path / "Scripts" / "Activate.ps1").is_file()
        or (dir_path / "bin" / "activate").is_file()
    )


def create_venv(dir_path):
    # Create a new virtual environment
    subprocess.run([sys.executable, "-m", "venv", str(dir_path)])


def get_venv_activation_cmd(venv_path):
    if sys.platform.startswith("win"):
        activation_cmd = str(venv_path / "Scripts" / "Activate.ps1")
    else:
        activation_cmd = f". {str(venv_path / 'bin' / 'activate')}"

    return activation_cmd


def install_dependencies_in_venv(venv_path, requirements_file_path):
    activation_cmd = get_venv_activation_cmd(venv_path)

    # Upgrade pip
    install_cmd = "pip install --upgrade pip"
    subprocess.run(f"{activation_cmd} && {install_cmd}", shell=True)

    # Install dependencies from requirements.txt
    install_cmd = f"pip install -r {str(requirements_file_path)}"
    subprocess.run(f"{activation_cmd} && {install_cmd}", shell=True)


if __name__ == "__main__":
    venv_path = Path(".venv")

    if not venv_path.exists() or not is_venv(venv_path):
        if venv_path.exists():
            shutil.rmtree(venv_path)
        create_venv(venv_path)

    install_dependencies_in_venv(venv_path, "requirements.txt")