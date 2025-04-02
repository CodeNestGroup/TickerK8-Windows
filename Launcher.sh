#!/bin/bash

# Find main folder of applcation.
PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

echo "PROJECT_DIR: $PROJECT_DIR"

# Check, if python is installed.
if ! command -v python3 &> /dev/null; then
    echo "Python3 nie jest zainstalowany. Pobieranie wersji portable..."
    curl -o python.tar.gz https://www.python.org/ftp/python/3.11.4/Python-3.11.4.tgz
    tar -xzf python.tar.gz -C "$PROJECT_DIR"
    PYTHON_EXEC="$PROJECT_DIR/python/bin/python3"
else
    PYTHON_EXEC="python3"
fi

# Create virtual enviroment.
if [ ! -d "$VENV_DIR" ]; then
    echo "Tworzenie wirtualnego środowiska..."
    $PYTHON_EXEC -m venv "$VENV_DIR"
fi

# Active virtual enviroment.
source "$VENV_DIR/bin/activate"

# Install packages.
pip install --upgrade pip
pip install -r "$PROJECT_DIR/TickerK8_updater/APP_FILES/CONFIG/requirements.txt"

# Start application.
python "$PROJECT_DIR/TickerK8_updater/APP_FILES/PYTHON/_00_main.py"
