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
REM FORCE PYTHON INSTALL
REM =========================
echo [INFO] Wymuszona instalacja Python 3.14.2...

set "PY_VERSION=3.14.2"
set "PY_INSTALLER=python-%PY_VERSION%-amd64.exe"
set "PY_URL=https://www.python.org/ftp/python/%PY_VERSION%/%PY_INSTALLER%"

REM Docelowa ścieżka (stała i przewidywalna)
set "PY_DIR=%LocalAppData%\Programs\Python\Python314"
set "PYTHON_CMD=%PY_DIR%\python.exe"

REM Usuń starą instalację lokalną (opcjonalnie)
if exist "%PY_DIR%" (
    echo [INFO] Usuwanie starej instalacji lokalnej...
    rmdir /s /q "%PY_DIR%" 2>nul
)

REM Pobierz instalator
powershell -Command "Invoke-WebRequest '%PY_URL%' -OutFile '%PY_INSTALLER%'"

if not exist "%PY_INSTALLER%" (
    echo [ERROR] Nie udalo sie pobrac Pythona
    pause
    exit /b 1
)

REM Instalacja (bez PATH, bez zgadywania)
echo [INFO] Instalacja Pythona...

start /wait "" "%PY_INSTALLER%" ^
    /quiet InstallAllUsers=0 ^
    TargetDir="%PY_DIR%" ^
    Include_test=0 ^
    Include_launcher=1 ^
    SimpleInstall=1

REM Sprawdzenie instalacji
if not exist "%PYTHON_CMD%" (
    echo [ERROR] Python nie zostal poprawnie zainstalowany
    pause
    exit /b 1
)

echo [INFO] Python OK: %PYTHON_CMD%

REM =========================
REM CREATE VENV FUNCTION
REM =========================
:CREATE_VENV
echo.
echo [INFO] Tworzenie venv...

if exist "%VENV_DIR%" (
    rmdir /s /q "%VENV_DIR%" 2>nul
)

"%PYTHON_CMD%" -m venv "%VENV_DIR%"

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo [ERROR] Nie udalo sie utworzyc venv
    pause
    exit /b 1
)

goto :eof

REM =========================
REM CHECK VENV
REM =========================
if not exist "%VENV_DIR%\Scripts\python.exe" (
    call :CREATE_VENV
)

set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

REM =========================
REM CHECK PIP
REM =========================
"%VENV_PY%" -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo [WARN] pip uszkodzony → rebuild venv
    call :CREATE_VENV
)

REM =========================
REM UPGRADE PIP
REM =========================
echo [INFO] Aktualizacja pip...
"%VENV_PY%" -m pip install --upgrade pip

REM =========================
REM INSTALL REQUIREMENTS
REM =========================
if not exist "%REQ_FILE%" (
    echo [ERROR] Brak requirements:
    echo %REQ_FILE%
    pause
    exit /b 1
)

echo [INFO] Instalacja zaleznosci...
"%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%"

if %errorlevel% neq 0 (
    echo [WARN] Blad instalacji → reset venv

    call :CREATE_VENV
    "%VENV_PY%" -m pip install --upgrade pip
    "%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%"
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
"%VENV_PY%" "%APP_FILE%"

pause