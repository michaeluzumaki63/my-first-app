from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Portfolio", docs_url=None, redoc_url=None, openapi_url=None)

_PAGE = (Path(__file__).resolve().parent / "templates" / "index.html").read_text(encoding="utf-8")


@app.get("/", response_class=HTMLResponse)
def root() -> HTMLResponse:
    return HTMLResponse(_PAGE)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
