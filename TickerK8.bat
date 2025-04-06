@echo off
setlocal

:: Set main folder
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%\.venv

:: Set path to python in venv
set PYTHON_EXEC=%VENV_DIR%\Scripts\python.exe

:: Check if _0000_app_base.py exists
if not exist "%PROJECT_DIR%\TickerK8_app\app_files\PYTHON\_0000_app_base.py" (
    echo [ERROR] File _0000_app_base not exists!
    pause
    exit /b 1
)

:: Starting application
start "TickerK8" cmd /c "%PYTHON_EXEC% \"%PROJECT_DIR%\\TickerK8_app\app_files\PYTHON\_0000_app_base.py\""

echo TickerK8 opened
exit /b 0
