@echo off
setlocal enabledelayedexpansion

echo START

set PROJECT_DIR=%~dp0
set PROJECT_DIR=%PROJECT_DIR:~0,-1%
set VENV_DIR=%PROJECT_DIR%\.venv
set REQ_FILE=%PROJECT_DIR%\updater\CONFIG\requirements.txt

set LOG_FILE=%PROJECT_DIR%\error_log.txt

where python >nul 2>nul
if %errorlevel%==0 (
    set PYTHON_EXEC=python
) else (
    set PYTHON_EXEC=
)

if not defined PYTHON_EXEC (
    set PY_URL=https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe
    set PY_INSTALLER=%PROJECT_DIR%\python_installer.exe

    powershell -Command "Invoke-WebRequest -Uri '%PY_URL%' -OutFile '%PY_INSTALLER%'"
    if not exist "%PY_INSTALLER%" (
        echo DOWNLOAD FAIL>>"%LOG_FILE%"
        pause
        exit /b 1
    )

    "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
    timeout /t 5 >nul

    if exist "%LocalAppData%\Programs\Python\Python314\python.exe" (
        set PYTHON_EXEC=%LocalAppData%\Programs\Python\Python314\python.exe
    )

    if not defined PYTHON_EXEC (
        where python >nul 2>nul
        if %errorlevel%==0 set PYTHON_EXEC=python
    )

    if not defined PYTHON_EXEC (
        echo PYTHON FAIL>>"%LOG_FILE%"
        pause
        exit /b 1
    )
)

set VENV_PY=%VENV_DIR%\Scripts\python.exe

if not exist "%VENV_DIR%" (
    %PYTHON_EXEC% -m venv "%VENV_DIR%" || goto error
)

if not exist "%VENV_PY%" goto error

"%VENV_PY%" -m pip install --upgrade pip >nul 2>&1 || goto error
"%VENV_PY%" -m pip install certifi >nul 2>&1

"%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%" || (
    rmdir /s /q "%VENV_DIR%"
    %PYTHON_EXEC% -m venv "%VENV_DIR%" || goto error
    "%VENV_PY%" -m pip install --upgrade pip >nul 2>&1
    "%VENV_PY%" -m pip install certifi >nul 2>&1
    "%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%" || goto error
)

"%VENV_PY%" "%PROJECT_DIR%\updater\PYTHON\__core__.py" || goto error

echo DONE
pause
exit /b 0

:error
echo CRASH>>"%LOG_FILE%"
echo ERROR - check log: %LOG_FILE%
pause
exit /b 1