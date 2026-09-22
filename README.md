# Portfolio

A one-page portfolio served by FastAPI. It says that I develop a website that provides software as a service, and it leaves the product unnamed.

Live: https://my-first-app-cp7j.onrender.com

## Run

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/ . Health check: http://127.0.0.1:8000/health .

Render deploys the `main` branch of this repo with:

- Build: `pip install -r requirements.txt`
- Start: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
