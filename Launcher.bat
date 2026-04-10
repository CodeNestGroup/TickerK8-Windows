@echo off
setlocal enabledelayedexpansion

REM --- katalog projektu ---
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%.venv
set REQ_FILE=%PROJECT_DIR%updater\CONFIG\requirements.txt

echo PROJECT_DIR: %PROJECT_DIR%

REM --- znajdź python ---
where python >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_EXEC=python
) else (
    echo [ERROR] Python nie znaleziony!
    echo Zainstaluj Python: https://www.python.org/downloads/windows/
    pause
    exit /b 1
)

REM --- funkcja create_venv ---
:CREATE_VENV
echo Tworzenie virtualenv...
rmdir /s /q "%VENV_DIR%" 2>nul
%PYTHON_EXEC% -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    echo [ERROR] Nie udało się stworzyć venv
    pause
    exit /b 1
)
goto :eof

REM --- jeśli brak venv ---
if not exist "%VENV_DIR%" (
    call :CREATE_VENV
)

REM --- aktywacja ---
call "%VENV_DIR%\Scripts\activate.bat"

REM --- sprawdź pip ---
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip uszkodzony → rebuild venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
)

echo Aktualizacja pip...
python -m pip install --upgrade pip

echo Instalacja zależności...
pip install --upgrade --no-cache-dir -r "%REQ_FILE%"

if %errorlevel% neq 0 (
    echo Błąd instalacji → reset venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
    python -m pip install --upgrade pip
    pip install --no-cache-dir -r "%REQ_FILE%"
)

echo Start aplikacji...
python "%PROJECT_DIR%updater\PYTHON\__core__.py"

pause