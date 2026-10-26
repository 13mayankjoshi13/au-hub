
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from backend.app.db.connection import check_database_connection

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
    database_healthy = check_database_connection()

    if not database_healthy:
        return JSONResponse(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            content={
                "status": "unhealthy",
                "service": "au-hub-api",
                "database": "disconnected",
            },
        )

    return {
        "status": "healthy",
        "service": "au-hub-api",
        "database": "connected",
    }
