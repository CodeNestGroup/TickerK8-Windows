@echo off
setlocal enabledelayedexpansion

:: Set main folder
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%\.venv

echo PROJECT_DIR: %PROJECT_DIR%

:: Check if python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Downloading portable version ...
    curl -o python.zip https://www.python.org/ftp/python/3.11.4/python-3.11.4-embed-amd64.zip
    powershell -Command "Expand-Archive -Path python.zip -DestinationPath %PROJECT_DIR%\python"
    set PYTHON_EXEC=%PROJECT_DIR%\python\python.exe
) else (
    set PYTHON_EXEC=python
)

:: Creating venv if not exists
if not exist "%VENV_DIR%" (
    echo Creating venv...
    %PYTHON_EXEC% -m venv "%VENV_DIR%" 
)

:: Set path to python in venv
set PIP_EXEC=%VENV_DIR%\Scripts\python.exe -m pip
set PYTHON_EXEC=%VENV_DIR%\Scripts\python.exe

:: Checkig if python is working in venv
echo Check version of Python in venv...
%PYTHON_EXEC% --version || (
    echo [ERROR] Could not started python in venv!
    pause
    exit /b 1
)

:: Install requirments
echo Installing requirements...
%PIP_EXEC% install --upgrade pip || (
    echo [ERROR] Install pip error! 
    pause
    exit /b 1
)
%PIP_EXEC% install -r "%PROJECT_DIR%\TickerK8_updater\APP_FILES\CONFIG\requirements.txt" || (
    echo [ERROR] Install requirements error!
    pause
    exit /b 1
)

:: Check if file _00_main.py exists
if not exist "%PROJECT_DIR%\TickerK8_updater\APP_FILES\PYTHON\_00_main.py" (
    echo [ERROR] File _00_main.py not exists!
    pause
    exit /b 1
)

:: Starting application
echo Starting application...
%PYTHON_EXEC% "%PROJECT_DIR%\TickerK8_updater\APP_FILES\PYTHON\_00_main.py" || (
    echo [ERROR] Error with starting application!
    pause
    exit /b 1
)
