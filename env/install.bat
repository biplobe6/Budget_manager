@echo off

(
    python3 -m venv .
    echo "Please configure firewall (if required)"
    pause
    Scripts\activate
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
)
