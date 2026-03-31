# Mifos Gazelle IaC Security Prototype

Standalone prototype repository for Infrastructure-as-Code security checks aligned to the Mifos Gazelle project idea.

This repository now includes both:
- CLI scanner mode (local Terraform path scan)
- Web scanner mode (single-page UI where a repo URL is submitted and scanned)

## What This Is

This repository contains a working scanner toolkit that supports both command-line and browser-based workflows.

CLI mode scans local Terraform files and prints rich severity output with optional CSV/PDF reports.

Web mode provides a minimal single-page frontend (no dashboard side tabs) that accepts a repository URL and runs backend scanning.

This is a prototype to demonstrate implementation readiness and delivery approach for Mifos Gazelle style IaC security gating.

## Current Capabilities

- Local Terraform security scanning via CLI
- Repository URL scan via web API
- Severity-based findings table (Critical/High/Medium/Low)
- Optional report export:
  - CSV report
  - PDF audit report
- File-level or directory-level scan target support

## Mifos Alignment

This prototype is designed to show how secure-by-default checks can be enforced before deployment:

- Scan IaC changes early
- Highlight risky misconfigurations
- Produce reviewer-friendly output
- Extend toward CI pull request policy gates

Planned extensions for full Mifos workflow:
- Checkov and Terrascan integration
- KubeLinter for Helm/Kubernetes manifests
- Gitleaks pre-commit and CI secret detection
- CI fail gate for Critical/High findings

## Prerequisites

1. Python 3.9+
2. tfsec installed and available in PATH

Windows (Chocolatey):

```powershell
choco install tfsec
```

Verify:

```powershell
tfsec --version
```

## Install and Run

From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
pip install -e .
```

Run help:

```powershell
mifos-gazelle-iac --help
```

Run a scan against a folder:

```powershell
mifos-gazelle-iac iac .\
```

Run a scan against one terraform file:

```powershell
mifos-gazelle-iac iac .\test_vulnerable.tf
```

Generate reports:

```powershell
mifos-gazelle-iac iac .\test_vulnerable.tf --csv-export --pdf-export
```

## Run Web App (Single-page frontend + backend)

Fastest way from project root:

```powershell
python run_web.py
```

Or run from webapp directory:

1. Move into web app directory:

```powershell
cd webapp
```

2. Create environment file:

```powershell
copy .env.example .env
```

3. Start backend (serves frontend on the same port):

```powershell
python run.py
```

4. Open in browser:

http://localhost:5000

5. Enter repository URL and click Run Scan.

API endpoints used by frontend:
- POST /api/mifos-gazelle/iac/scan
- GET /api/mifos-gazelle/iac/export?scanId=<id>&format=pdf|csv
