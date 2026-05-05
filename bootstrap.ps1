# SOVEREIGN Bootstrap Script

Write-Host "Bootstrapping SOVEREIGN..."

# Check if running as administrator
if (-not ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)) {
    Write-Host "Please run this script as an Administrator." -ForegroundColor Red
    exit 1
}

# Create necessary directories
$dirs = @("build", "logs", "temp")
foreach ($dir in $dirs) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir | Out-Null
        Write-Host "Created directory: $dir"
    }
}

# Check for required tools
$requiredTools = @("python", "git", "make")
foreach ($tool in $requiredTools) {
    if (Get-Command $tool -ErrorAction SilentlyContinue) {
        Write-Host "$tool is available"
    } else {
        Write-Host "$tool is not available. Please install it." -ForegroundColor Yellow
    }
}

Write-Host "Bootstrap complete. Run 'python -m pip install -r requirements.txt' to install dependencies."