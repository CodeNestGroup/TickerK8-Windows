@echo off
setlocal enabledelayedexpansion

REM =========================
REM CONFIG
REM =========================
set "PROJECT_DIR=%~dp0"
set "VENV_DIR=%PROJECT_DIR%.venv"
set "REQ_FILE=%PROJECT_DIR%updater\CONFIG\requirements.txt"
set "APP_FILE=%PROJECT_DIR%updater\PYTHON\__core__.py"

echo =========================================
echo PROJECT_DIR: %PROJECT_DIR%
echo =========================================

REM =========================
REM FIND PYTHON (py launcher preferred)
REM =========================
where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python"
    ) else (
        echo [ERROR] Nie znaleziono Pythona (py ani python)
        echo Zainstaluj: https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

echo Using Python: %PYTHON_CMD%

REM =========================
REM FUNCTION: CREATE VENV
REM =========================
:CREATE_VENV
echo.
echo [INFO] Tworzenie virtualenv...

if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%" 2>nul
)

%PYTHON_CMD% -m venv "%VENV_DIR%"

if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [ERROR] Nie udalo sie utworzyc venv
    echo Sprawdz instalacje Pythona i uprawnienia folderu
    pause
    exit /b 1
)

goto :eof

REM =========================
REM CHECK VENV
REM =========================
if not exist "%VENV_DIR%\Scripts\activate.bat" (
    call :CREATE_VENV
)

REM =========================
REM ACTIVATE VENV
REM =========================
call "%VENV_DIR%\Scripts\activate.bat"

if %errorlevel% neq 0 (
    echo [ERROR] Nie udalo sie aktywowac venv
    pause
    exit /b 1
)

REM =========================
REM CHECK PIP
REM =========================
python -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARN] Pip uszkodzony - reset venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
)

REM =========================
REM UPGRADE PIP
REM =========================
echo.
echo [INFO] Aktualizacja pip...
python -m pip install --upgrade pip

if %errorlevel% neq 0 (
    echo [ERROR] Nie udalo sie zaktualizowac pip
    pause
    exit /b 1
)

REM =========================
REM INSTALL REQUIREMENTS
REM =========================
if not exist "%REQ_FILE%" (
    echo [ERROR] Brak pliku requirements:
    echo %REQ_FILE%
    pause
    exit /b 1
)

echo.
echo [INFO] Instalacja zaleznosci...
pip install --no-cache-dir -r "%REQ_FILE%"

if %errorlevel% neq 0 (
    echo [WARN] Blad instalacji - reset venv i retry

    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"

    python -m pip install --upgrade pip
    pip install --no-cache-dir -r "%REQ_FILE%"
)

REM =========================
REM RUN APP
REM =========================
if not exist "%APP_FILE%" (
    echo [ERROR] Brak pliku aplikacji:
    echo %APP_FILE%
    pause
    exit /b 1
)

echo.
echo [INFO] Start aplikacji...
python "%APP_FILE%"

echo.
echo [INFO] Zakonczono.
pause