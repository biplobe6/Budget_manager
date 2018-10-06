@echo off

(
    python3 -m venv .
    echo "Please configure firewall (if required)"
    pause
    Scripts\activate
    python.exe -m pip install pip --upgrade
    pip install -r requirments.txt
)
