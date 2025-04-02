@echo off
setlocal enabledelayedexpansion

:: Ustalanie katalogu głównego projektu
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%\.venv

echo PROJECT_DIR: %PROJECT_DIR%

:: Sprawdzenie, czy Python jest zainstalowany
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python nie jest zainstalowany. Pobieranie wersji portable...
    curl -o python.zip https://www.python.org/ftp/python/3.11.4/python-3.11.4-embed-amd64.zip
    powershell -Command "Expand-Archive -Path python.zip -DestinationPath %PROJECT_DIR%\python"
    set PYTHON_EXEC=%PROJECT_DIR%\python\python.exe
) else (
    set PYTHON_EXEC=python
)

:: Tworzenie wirtualnego środowiska, jeśli nie istnieje
if not exist "%VENV_DIR%" (
    echo Tworzenie wirtualnego środowiska...
    %PYTHON_EXEC% -m venv "%VENV_DIR%"
)

:: Ustawienie ścieżki do Pythona w virtualenv
set PIP_EXEC=%VENV_DIR%\Scripts\python.exe -m pip
set PYTHON_EXEC=%VENV_DIR%\Scripts\python.exe

:: Sprawdzenie czy Python w venv działa
echo Sprawdzanie wersji Pythona w venv...
%PYTHON_EXEC% --version || (
    echo [BŁĄD] Nie udało się uruchomić Pythona w venv!
    pause
    exit /b 1
)

:: Instalacja zależności
echo Instalacja zależności...
%PIP_EXEC% install --upgrade pip || (
    echo [BŁĄD] Instalacja pip nie powiodła się!
    pause
    exit /b 1
)
%PIP_EXEC% install -r "%PROJECT_DIR%\TickerK8_updater\APP_FILES\CONFIG\requirements.txt" || (
    echo [BŁĄD] Instalacja zależności nie powiodła się!
    pause
    exit /b 1
)

:: Sprawdzenie czy plik _00_main.py istnieje
if not exist "%PROJECT_DIR%\TickerK8_updater\APP_FILES\PYTHON\_00_main.py" (
    echo [BŁĄD] Plik _00_main.py nie istnieje!
    pause
    exit /b 1
)

:: Uruchomienie aplikacji
echo Uruchamianie aplikacji...
%PYTHON_EXEC% "%PROJECT_DIR%\TickerK8_updater\APP_FILES\PYTHON\_00_main.py" || (
    echo [BŁĄD] Nie udało się uruchomić aplikacji!
    pause
    exit /b 1
)
