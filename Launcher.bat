@echo off
setlocal enabledelayedexpansion

REM =========================
REM PROJECT SETUP
REM =========================
set "PROJECT_DIR=%~dp0"
set "VENV_DIR=%PROJECT_DIR%.venv"
set "REQ_FILE=%PROJECT_DIR%updater\CONFIG\requirements.txt"
set "APP_FILE=%PROJECT_DIR%updater\PYTHON\__core__.py"

echo =========================================
echo PROJECT_DIR: %PROJECT_DIR%
echo =========================================

REM =========================
REM CHECK / INSTALL PYTHON
REM =========================
where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py -3"
    goto PY_OK
)

where python >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=python"
    goto PY_OK
)

echo [INFO] Python nie znaleziony - instalacja...

set "PY_VERSION=3.14.0"
set "PY_INSTALLER=python-%PY_VERSION%-amd64.exe"
set "PY_URL=https://www.python.org/ftp/python/%PY_VERSION%/%PY_INSTALLER%"

powershell -Command "Invoke-WebRequest '%PY_URL%' -OutFile '%PY_INSTALLER%'"

if not exist "%PY_INSTALLER%" (
    echo [ERROR] Nie udalo sie pobrac Pythona
    pause
    exit /b 1
)

echo Instalacja Pythona...

start /wait "" "%PY_INSTALLER%" ^
    /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

where py >nul 2>nul
if %errorlevel%==0 (
    set "PYTHON_CMD=py -3"
) else (
    where python >nul 2>nul
    if %errorlevel%==0 (
        set "PYTHON_CMD=python"
    ) else (
        echo [ERROR] Instalacja Pythona nie powiodla sie
        pause
        exit /b 1
    )
)

:PY_OK
echo Using Python: %PYTHON_CMD%

REM =========================
REM CREATE VENV FUNCTION
REM =========================
:CREATE_VENV
echo.
echo [INFO] Tworzenie venv...

if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%" 2>nul
)

%PYTHON_CMD% -m venv "%VENV_DIR%"

if not exist "%VENV_DIR%\Scripts\activate.bat" (
    echo [ERROR] Nie udalo sie utworzyc venv
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
    echo [WARN] pip uszkodzony → rebuild venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
)

REM =========================
REM UPGRADE PIP
REM =========================
echo [INFO] Aktualizacja pip...
python -m pip install --upgrade pip

REM =========================
REM INSTALL REQUIREMENTS (with retry)
REM =========================
if not exist "%REQ_FILE%" (
    echo [ERROR] Brak requirements:
    echo %REQ_FILE%
    pause
    exit /b 1
)

echo [INFO] Instalacja zaleznosci...
pip install --no-cache-dir -r "%REQ_FILE%"

if %errorlevel% neq 0 (
    echo [WARN] Blad instalacji → reset venv

    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"

    python -m pip install --upgrade pip
    pip install --no-cache-dir -r "%REQ_FILE%"
)

REM =========================
REM RUN APP
REM =========================
if not exist "%APP_FILE%" (
    echo [ERROR] Brak aplikacji:
    echo %APP_FILE%
    pause
    exit /b 1
)

echo.
echo [INFO] Start aplikacji...
python "%APP_FILE%"

pause