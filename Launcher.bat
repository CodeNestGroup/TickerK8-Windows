@echo off
setlocal enabledelayedexpansion

REM --- katalog projektu ---
set PROJECT_DIR=%~dp0
set PROJECT_DIR=%PROJECT_DIR:~0,-1%
set VENV_DIR=%PROJECT_DIR%\.venv
set REQ_FILE=%PROJECT_DIR%\updater\CONFIG\requirements.txt

echo PROJECT_DIR: %PROJECT_DIR%

REM --- znajdź python ---
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python nie znaleziony. Instalacja Python 3.14.2...

    set PY_URL=https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe
    set PY_INSTALLER=%PROJECT_DIR%\python_installer.exe

    echo Pobieranie...
    powershell -Command "Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%PY_INSTALLER%'"

    if not exist "%PY_INSTALLER%" (
        echo [ERROR] Nie udało się pobrać instalatora
        pause
        exit /b 1
    )

    echo Instalacja (silent)...
    "%PY_INSTALLER%" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    echo Czekanie na zakończenie instalacji...
    timeout /t 10 >nul

    REM --- odśwież PATH ---
    call refreshenv >nul 2>nul

    where python >nul 2>nul
    if %errorlevel% neq 0 (
        echo [ERROR] Python nadal niewidoczny po instalacji.
        echo Spróbuj uruchomić ponownie system lub terminal.
        pause
        exit /b 1
    )
)

set PYTHON_EXEC=python

REM --- funkcja create_venv ---
:CREATE_VENV
echo Tworzenie virtualenv...
if exist "%VENV_DIR%" rmdir /s /q "%VENV_DIR%"
%PYTHON_EXEC% -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    echo [ERROR] Nie udało się utworzyć venv
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
"%VENV_DIR%\Scripts\python.exe" -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip uszkodzony → rebuild venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
)

echo Aktualizacja pip...
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip >nul

echo Instalacja zależności...

REM --- instalacja z retry ---
"%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade --no-cache-dir -r "%REQ_FILE%"
if %errorlevel% neq 0 (
    echo Błąd instalacji → pełny reset venv
    call :CREATE_VENV
    call "%VENV_DIR%\Scripts\activate.bat"
    "%VENV_DIR%\Scripts\python.exe" -m pip install --upgrade pip
    "%VENV_DIR%\Scripts\python.exe" -m pip install --no-cache-dir -r "%REQ_FILE%"
)

echo Start aplikacji...
"%VENV_DIR%\Scripts\python.exe" "%PROJECT_DIR%\updater\PYTHON\__core__.py"

endlocal