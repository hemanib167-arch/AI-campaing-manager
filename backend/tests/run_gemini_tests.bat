@echo off
REM Quick script to run Gemini API tests on Windows

echo ============================================================
echo Gemini API Testing Script
echo ============================================================
echo.

REM Check if python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check and install required packages
python -c "import google.generativeai" >nul 2>&1
if errorlevel 1 (
    echo Installing required packages...
    pip install google-generativeai google-genai Pillow httpx
    echo.
)

REM Run the unified test runner
python run_all_gemini_tests.py %*

echo.
pause
