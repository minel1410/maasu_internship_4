import os
import subprocess
import shutil
import sys
from pathlib import Path


def build_apidoc(apidoc_path):
    # Remove apidoc-generated output dirs
    if apidoc_path.exists():
        shutil.rmtree(apidoc_path)

    # Running APIDOC
    apidoc_command = [
        "sphinx-apidoc",
        "--module-first",
        "--implicit-namespaces",
        "--separate",
        "-f",
        "-o",
        str(apidoc_path),
        str(Path("..") / "src"),
    ]

    result = subprocess.run(apidoc_command)
    if result.returncode != 0:
        raise RuntimeError("Execution of 'sphinx-apidoc' failed")


def build_html_docs():
    shell = False
    if sys.platform.startswith("win"):
        clean_command = [".\\make", "clean"]
        html_command = [".\\make", "html"]
        shell = True

    else:
        clean_command = ["make", "clean"]
        html_command = ["make", "html"]

    # Running CLEAN
    result = subprocess.run(clean_command, shell=shell)
    if result.returncode != 0:
        raise RuntimeError("Execution of 'make clean' failed")

    # Building HTML
    subprocess.run(html_command, shell=shell)
    if result.returncode != 0:
        raise RuntimeError("Execution of 'make html' failed")


if __name__ == "__main__":
    # Change cwd to the 'docs' directory
    docs_path = Path("docs").resolve()
    os.chdir(docs_path)

    apidoc_path = Path("source") / "apidoc"
    build_apidoc(apidoc_path)
    build_html_docs()