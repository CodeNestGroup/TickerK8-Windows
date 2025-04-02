@echo off
setlocal

:: Ustalanie katalogu głównego projektu
set PROJECT_DIR=%~dp0
set VENV_DIR=%PROJECT_DIR%\.venv

:: Ustawienie ścieżki do Pythona w virtualenv
set PYTHON_EXEC=%VENV_DIR%\Scripts\python.exe

:: Sprawdzenie czy plik nowej aplikacji istnieje
if not exist "%PROJECT_DIR%\TickerK8_app\app_files\PYTHON\_0000_app_base.py" (
    echo [BŁĄD] Plik main.py nie istnieje!
    pause
    exit /b 1
)

:: Uruchomienie nowej aplikacji w osobnym oknie
start "Nowa Aplikacja" cmd /c "%PYTHON_EXEC% \"%PROJECT_DIR%\\TickerK8_app\app_files\PYTHON\_0000_app_base.py\""

echo Nowa aplikacja została uruchomiona.
exit /b 0
