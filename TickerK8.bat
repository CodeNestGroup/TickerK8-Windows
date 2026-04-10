@echo off

set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%.venv

call "%VENV_DIR%\Scripts\activate.bat"

python "%PROJECT_DIR%TickerK8_app\APP_FILES\PYTHON\__core__.py"

pause