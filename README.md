# Product Catalog Team Demo

Synthetic FastAPI repository for demonstrating GitHub Copilot custom agents through a feature request.

## Feature request
Add an optional `in_stock_only` filter to `GET /products` without changing the current default response.

## Local setup

```powershell
py -m venv .venv
& ".\.venv\Scripts\python.exe" -m pip install -r requirements.txt
& ".\.venv\Scripts\python.exe" -m pytest -q
```
