# --- Configuration ---
$VenvDir = "venv"
$ReqFile = "requirements.txt"
$EnvFile = ".env_vars.ps1"
$MainScript = "main.py"
$NeedInput = $false

# --- Check or create virtual environment ---
if (-Not (Test-Path "$VenvDir")) {
    Write-Host "Creating virtual environment..."
    python -m venv $VenvDir
    & "$VenvDir\Scripts\Activate.ps1"
    Write-Host "Installing dependencies from $ReqFile..."
    pip install --upgrade pip
    pip install -r $ReqFile
} else {
    & "$VenvDir\Scripts\Activate.ps1"
}

# --- Load or check environment variables ---
if (Test-Path $EnvFile) {
    . .\$EnvFile
    $Now = [int][double]::Parse((Get-Date -UFormat %s))
    $Age = $Now - $env:LAST_SET
    if ($Age -gt 86400) {
        Write-Host "Environment variables are older than 24 hours. Please re-enter them."
        $NeedInput = $true
    }
} else {
    $NeedInput = $true
}

# --- If needed: Prompt for environment variables ---
if ($NeedInput) {
    $user = Read-Host "Username"
    $token = Read-Host -AsSecureString "Token"
    $plainToken = [Runtime.InteropServices.Marshal]::PtrToStringAuto(
        [Runtime.InteropServices.Marshal]::SecureStringToBSTR($token)
    )

    $env:USER = $user
    $env:TOKEN = $plainToken
    $now = [int][double]::Parse((Get-Date -UFormat %s))

    Set-Content -Path $EnvFile -Value @(
        "`$env:USER = `"$user`""
        "`$env:TOKEN = `"$plainToken`""
        "`$env:LAST_SET = $now"
    )
}

# --- Run the Python script ---
python $MainScript
