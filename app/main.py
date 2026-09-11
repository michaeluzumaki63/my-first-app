from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Welcome to my-first-app"}


@app.get("/health")
def health():
    return {"status": "ok"}
