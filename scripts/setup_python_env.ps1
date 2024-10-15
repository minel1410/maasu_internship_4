if (!(Test-Path -Path .venv/Scripts/Activate.ps1)) {
    Remove-Item -Path .venv -Recurse -Force -ErrorAction SilentlyContinue
    python -m venv .venv
}
.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt