
from fastapi import FastAPI

app = FastAPI(
    title="AU Hub API",
    description=(
        "Learning, collaboration, academic resources, "
        "quizzes, and machine learning for the "
        "Amrapali University community."
    ),
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "success": True,
        "message": "AU Hub API is running.",
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "au-hub-api",
    }
