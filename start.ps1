# 6E Creative Studio — Windows Start Script (no Docker)
# Usage: Right-click → Run with PowerShell  OR  pwsh start.ps1

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "   6E Creative Studio — Dev Launcher   " -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

# ── 0. Copy .env if it doesn't exist ─────────────────────────────────────────
if (-not (Test-Path ".\.env")) {
    Copy-Item ".\.env.example" ".\.env"
    Write-Host "[INFO] Created .env from .env.example — fill in your OPENAI_API_KEY!" -ForegroundColor Yellow
}

# ── 1. Backend — create venv, install deps, start uvicorn ────────────────────
Write-Host "`n[BACKEND] Setting up Python virtual environment..." -ForegroundColor Green

Set-Location "backend"

if (-not (Test-Path ".\venv")) {
    python -m venv venv
    Write-Host "[BACKEND] venv created." -ForegroundColor Green
}

.\venv\Scripts\Activate.ps1
pip install -r requirements.txt --quiet

Write-Host "[BACKEND] Starting FastAPI on http://localhost:8000 ..." -ForegroundColor Green
$backendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    .\venv\Scripts\python.exe -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
}

Set-Location ".."

# ── 2. Frontend — npm install + dev server ────────────────────────────────────
Write-Host "`n[FRONTEND] Installing npm packages..." -ForegroundColor Green
Set-Location "frontend"
npm install --silent

Write-Host "[FRONTEND] Starting Vite dev server on http://localhost:5173 ..." -ForegroundColor Green
$frontendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    npm run dev
}

Set-Location ".."

# ── 3. Print summary ──────────────────────────────────────────────────────────
Start-Sleep -Seconds 3
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "  Backend  → http://localhost:8000"      -ForegroundColor White
Write-Host "  API Docs → http://localhost:8000/docs" -ForegroundColor White
Write-Host "  Frontend → http://localhost:5173"      -ForegroundColor White
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nPress Ctrl+C to stop both servers.`n"  -ForegroundColor Yellow

# Keep script alive; kill both jobs on exit
try {
    Receive-Job -Job $backendJob, $frontendJob -Wait
} finally {
    Stop-Job $backendJob, $frontendJob
    Remove-Job $backendJob, $frontendJob
}
