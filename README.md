# ⚡ A starter example with FastAPI

## Clone to local

```bash
git clone https://github.com/xbmlz/fastapi-starter.git fastapi-app

cd fastapi-app
```

## Create virtual environment

```bash
python -m venv .env

# windows
.\.env\scripts\activate

# macos or linux
source .env/bin/activate
```

## Setup

```bash
pip install -r requirements.txt
```

## Development

```bash
python -m uvicorn app.main:app --host 0.0.0.0 --reload
```

## Document

[FastAPI](https://fastapi.tiangolo.com/)