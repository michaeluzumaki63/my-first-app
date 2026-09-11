# my-first-app

A clean FastAPI starter project with a welcome endpoint, health check, and Docker support.

## Install

```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

Then open http://127.0.0.1:8000/ and check health at http://127.0.0.1:8000/health.

## Docker

Build and run:

```bash
docker build -t my-first-app . && docker run -p 8000:8000 my-first-app
```
