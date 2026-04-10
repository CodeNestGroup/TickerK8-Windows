@echo off
setlocal EnableExtensions EnableDelayedExpansion

echo START

set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"
set "VENV_DIR=%PROJECT_DIR%\.venv"
set "REQ_FILE=%PROJECT_DIR%\updater\CONFIG\requirements.txt"
set "LOG_FILE=%PROJECT_DIR%\error_log.txt"

set "PYTHON_EXEC="

REM =========================
REM 1. Sprawdź istniejącego Pythona
REM =========================
where python >nul 2>nul
if not errorlevel 1 set "PYTHON_EXEC=python"

REM =========================
REM 2. Jeśli brak → instaluj 3.14.2
REM =========================
if not defined PYTHON_EXEC (
    echo Python not found, installing 3.14.2...

    set "PY_URL=https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe"
    set "PY_INSTALLER=%PROJECT_DIR%\python_installer.exe"

    powershell -NoProfile -ExecutionPolicy Bypass -Command ^
        "Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%PY_INSTALLER%'"

    if not exist "%PY_INSTALLER%" (
        echo DOWNLOAD FAIL>>"%LOG_FILE%"
        goto error
    )

    "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

    timeout /t 10 >nul

    REM =========================
    REM 3. Znajdź Python 3.14.x dynamicznie
    REM =========================
    for /d %%D in ("%LocalAppData%\Programs\Python\Python3*") do (
        if exist "%%D\python.exe" set "PYTHON_EXEC=%%D\python.exe"
    )

    REM fallback
    if not defined PYTHON_EXEC (
        where python >nul 2>nul && set "PYTHON_EXEC=python"
    )

    if not defined PYTHON_EXEC (
        echo PYTHON FAIL>>"%LOG_FILE%"
        goto error
    )
)

echo Using Python: %PYTHON_EXEC%

set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

REM =========================
REM 4. venv
REM =========================
if not exist "%VENV_DIR%" (
    "%PYTHON_EXEC%" -m venv "%VENV_DIR%" || goto error
)

if not exist "%VENV_PY%" goto error

REM =========================
REM 5. pip setup
REM =========================
"%VENV_PY%" -m pip install --upgrade pip >nul 2>&1 || goto error
"%VENV_PY%" -m pip install certifi >nul 2>&1

REM =========================
REM 6. requirements (retry)
REM =========================
"%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%"
if errorlevel 1 (
    echo Retry clean venv...

    rmdir /s /q "%VENV_DIR%"

    "%PYTHON_EXEC%" -m venv "%VENV_DIR%" || goto error

    "%VENV_PY%" -m pip install --upgrade pip >nul 2>&1
    "%VENV_PY%" -m pip install certifi >nul 2>&1
    "%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%" || goto error
)

REM =========================
REM 7. run core
REM =========================
"%VENV_PY%" "%PROJECT_DIR%\updater\PYTHON\__core__.py" || goto error

echo DONE
pause
exit /b 0

:error
echo CRASH>>"%LOG_FILE%"
echo ERROR - check log: %LOG_FILE%
pause
exit /b 1