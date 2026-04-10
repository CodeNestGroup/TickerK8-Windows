#!/bin/bash

PROJECT_DIR="$(cd "$(dirname "$0")"; pwd)"
VENV_DIR="$PROJECT_DIR/.venv"

source "$VENV_DIR/bin/activate"

python "$PROJECT_DIR/TickerK8_app/APP_FILES/PYTHON/__core__.py"