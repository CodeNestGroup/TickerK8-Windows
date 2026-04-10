@echo off
setlocal enabledelayedexpansion

echo ============================
echo START (ERROR ONLY MODE)
echo ============================

REM --- paths ---
set "PROJECT_DIR=%~dp0"
set "PROJECT_DIR=%PROJECT_DIR:~0,-1%"
set "VENV_DIR=%PROJECT_DIR%\.venv"
set "REQ_FILE=%PROJECT_DIR%\updater\CONFIG\requirements.txt"

set "PY_INSTALLER=%PROJECT_DIR%\python_installer.exe"
set "PY_URL=https://www.python.org/ftp/python/3.14.2/python-3.14.2-amd64.exe"

REM =====================================================
REM CHECK PYTHON
REM =====================================================

set "PYTHON_EXEC="

for %%P in (python py) do (
    where %%P >nul 2>nul
    if !errorlevel! == 0 (
        set "PYTHON_EXEC=%%P"
        goto :PY_FOUND
    )
)

echo Python not found → installing...

REM download python
powershell -NoProfile -Command ^
"try { Invoke-WebRequest '%PY_URL%' -OutFile '%PY_INSTALLER%' -UseBasicParsing } catch { exit 1 }"

if not exist "%PY_INSTALLER%" (
    echo ERROR: Python download failed
    goto END
)

REM install python silently
"%PY_INSTALLER%" /quiet InstallAllUsers=0 PrependPath=1 Include_test=0

timeout /t 10 >nul

REM re-check python
for %%P in (python py) do (
    where %%P >nul 2>nul
    if !errorlevel! == 0 (
        set "PYTHON_EXEC=%%P"
        goto :PY_FOUND
    )
)

echo ERROR: Python installation failed (not in PATH)
goto END

:PY_FOUND
REM =====================================================
REM VENV
REM =====================================================

if not exist "%VENV_DIR%\Scripts\python.exe" (
    echo Creating venv...

    %PYTHON_EXEC% -m venv "%VENV_DIR%" >nul 2>&1

    if not exist "%VENV_DIR%\Scripts\python.exe" (
        echo ERROR: venv creation failed
        goto END
    )
)

set "VENV_PY=%VENV_DIR%\Scripts\python.exe"

REM =====================================================
REM PIP CHECK
REM =====================================================

%VENV_PY% -m pip --version >nul 2>&1
if !errorlevel! neq 0 (
    echo ERROR: pip broken → rebuilding venv
    rmdir /s /q "%VENV_DIR%"
    goto :PY_FOUND
)

REM =====================================================
REM INSTALL REQUIREMENTS
REM =====================================================

%VENV_PY% -m pip install --upgrade pip >nul 2>&1

%VENV_PY% -m pip install -r "%REQ_FILE%" >nul 2>&1

if !errorlevel! neq 0 (
    echo ERROR: requirements install failed
)

REM =====================================================
REM RUN APP
REM =====================================================

if exist "%PROJECT_DIR%\updater\PYTHON\__core__.py" (
    %VENV_PY% "%PROJECT_DIR%\updater\PYTHON\__core__.py" >nul 2>&1

    if !errorlevel! neq 0 (
        echo ERROR: app crashed
    )
) else (
    echo ERROR: missing __core__.py
)

:END
echo.
echo DONE
pause
endlocal
exit /b