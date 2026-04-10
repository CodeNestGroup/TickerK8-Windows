@echo on
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
        echo [FATAL ERROR] Download fail
        pause
        goto END
    )

    "%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0
    timeout /t 5 >nul

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
        echo [FATAL ERROR] Python nadal niewidoczny
        pause
        goto END
    )
)

echo Python: %PYTHON_EXEC%

REM --- funkcja venv ---
:CREATE_VENV
echo ============================
echo TWORZENIE VENV
echo ============================

if exist "%VENV_DIR%" (
    echo Usuwam stary venv...
    rmdir /s /q "%VENV_DIR%"
)

echo Uruchamiam venv:
echo %PYTHON_EXEC% -m venv "%VENV_DIR%"

%PYTHON_EXEC% -m venv "%VENV_DIR%"
set VENV_ERR=%errorlevel%

echo ERRORLEVEL venv: !VENV_ERR!

if not "!VENV_ERR!"=="0" (
    echo [FATAL ERROR] venv creation failed
    pause
    goto END
)

goto :eof

REM --- tworzenie venv jeśli brak ---
if not exist "%VENV_DIR%" (
    call :CREATE_VENV
)

set VENV_PY=%VENV_DIR%\Scripts\python.exe

if not exist "%VENV_PY%" (
    echo [FATAL ERROR] brak python w venv
    pause
    goto END
)

REM --- pip check ---
"%VENV_PY%" -m pip --version >nul 2>nul
if not %errorlevel%==0 (
    echo pip broken → rebuild venv
    call :CREATE_VENV
)

echo ============================
echo UPDATE PIP
echo ============================
"%VENV_PY%" -m pip install --upgrade pip --verbose

echo ============================
echo CERTYFIKATY SSL
echo ============================
"%VENV_PY%" -m pip install certifi --verbose

echo ============================
echo INSTALACJA REQUIREMENTS
echo ============================
"%VENV_PY%" -m pip install --upgrade --no-cache-dir -r "%REQ_FILE%" --verbose

if not %errorlevel%==0 (
    echo [WARN] retry instalacji...

    call :CREATE_VENV

    "%VENV_PY%" -m pip install --upgrade pip --verbose
    "%VENV_PY%" -m pip install certifi --verbose
    "%VENV_PY%" -m pip install --no-cache-dir -r "%REQ_FILE%" --verbose
)

echo ============================
echo START APLIKACJI
echo ============================
"%VENV_PY%" "%PROJECT_DIR%\updater\PYTHON\__core__.py"

echo ERRORLEVEL APP: !errorlevel!

:END
echo.
echo ============================
echo KONIEC SKRYPTU
echo ============================
pause
endlocal
exit /b