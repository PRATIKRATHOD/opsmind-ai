from fastapi import FastAPI

app = FastAPI(title="OpsMind AI")


@app.get("/")
def home():
    return {
        "message": "OpsMind AI is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }