@echo off
setlocal enabledelayedexpansion

echo ============================
echo START SKRYPTU
echo ============================

REM --- katalog projektu ---
set PROJECT_DIR=%~dp0
set PROJECT_DIR=%PROJECT_DIR:~0,-1%
set VENV_DIR=%PROJECT_DIR%\.venv
set REQ_FILE=%PROJECT_DIR%\updater\CONFIG\requirements.txt

echo PROJECT_DIR: %PROJECT_DIR%

REM --- znajdź python ---
set PYTHON_EXEC=

where python >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_EXEC=python
)

REM --- jeśli brak → instalacja ---
if not defined PYTHON_EXEC (
    echo Python nie znaleziony. Instalacja Python 3.14.2...

    set PY_URL=https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe
    set PY_INSTALLER=%PROJECT_DIR%\python_installer.exe

    powershell -Command "Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%PY_INSTALLER%'"

    if not exist "%PY_INSTALLER%" (
        echo [ERROR] Download fail
        pause
        exit /b 1
    )

    "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

    timeout /t 5 >nul

    REM --- fallback ścieżki ---
    if exist "%LocalAppData%\Programs\Python\Python314\python.exe" (
        set PYTHON_EXEC=%LocalAppData%\Programs\Python\Python314\python.exe
    )

    if not defined PYTHON_EXEC (
        where python >nul 2>nul
        if %errorlevel%==0 (
            set PYTHON_EXEC=python
        )
    )

    if not defined PYTHON_EXEC (
        echo [ERROR] Python nadal niewidoczny
        pause
        exit /b 1
    )
)

echo Python: %PYTHON_EXEC%

REM --- funkcja create_venv ---
:CREATE_VENV
echo Tworzenie virtualenv...
if exist "%VENV_DIR%" rmdir /s /q "%VENV_DIR%"
%PYTHON_EXEC% -m venv "%VENV_DIR%"
if %errorlevel% neq 0 (
    echo [ERROR] venv fail
    pause
    exit /b 1
)
goto :eof

REM --- jeśli brak venv ---
if not exist "%VENV_DIR%" (
    call :CREATE_VENV
)

REM --- python z venv ---
set VENV_PY=%VENV_DIR%\Scripts\python.exe

REM --- sprawdź pip ---
"%VENV_PY%" -m pip --version >nul 2>nul
if %errorlevel% neq 0 (
    echo pip uszkodzony → rebuild
    call :CREATE_VENV
)

echo Aktualizacja pip...
"%VENV_PY%" -m pip install --upgrade pip

echo Naprawa SSL (certyfikaty)...
"%VENV_PY%" -m pip install certifi

echo Instalacja zależności...
"%VENV_PY%" -m pip install --upgrade --no-cache-dir -r "%REQ_FILE%"

if %errorlevel% neq 0 (
    echo Retry instalacji...
    call :CREATE_VENV
    "%VENV_PY%" -m pip install --upgrade pip
    "%VENV_PY%" -m pip install certifi
    "%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%"
)

echo Start aplikacji...
"%VENV_PY%" "%PROJECT_DIR%\updater\PYTHON\__core__.py"

echo.
echo ============================
echo KONIEC
echo ============================
pause
endlocal