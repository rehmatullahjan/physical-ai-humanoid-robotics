$ErrorActionPreference = "Stop"

Write-Host "Starting Physical AI Book & Chatbot..." -ForegroundColor Cyan

# Start Backend
Write-Host "Starting Chatbot Backend (Port 8000)..." -ForegroundColor Yellow
$backendProcess = Start-Process -FilePath ".\rag_chatbot\venv\Scripts\python.exe" -ArgumentList "rag_chatbot/api.py" -PassThru -NoNewWindow
if (-not $backendProcess) {
    Write-Error "Failed to start backend."
}

# Start Frontend
Write-Host "Starting Docusaurus Book (Port 3000)..." -ForegroundColor Green
Set-Location "book"
npm start
