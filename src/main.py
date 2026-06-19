from fastapi import FastAPI
from src.api.routes import router

app = FastAPI(
    title="AI Logic Flaw Auditor",
    version="0.1.0"
)

app.include_router(router)

@app.get("/")
def root():
    return {
        "project": "AI Logic Flaw Auditor",
        "status": "running"
    }
