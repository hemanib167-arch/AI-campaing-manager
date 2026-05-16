#!/bin/bash
# Quick script to run Gemini API tests on Linux/Mac

echo "============================================================"
echo "Gemini API Testing Script"
echo "============================================================"
echo ""

# Check if python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

# Check and install required packages
if ! python3 -c "import google.generativeai" &> /dev/null; then
    echo "Installing required packages..."
    pip3 install google-generativeai google-genai Pillow httpx
    echo ""
fi

# Run the unified test runner
python3 run_all_gemini_tests.py "$@"

echo ""
