
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

from backend.app.core.config import (
    API_PREFIX,
    APP_NAME,
    APP_VERSION,
)
from backend.app.db.connection import check_database_connection
from backend.app.routes.auth import router as auth_router


app = FastAPI(
    title=f"{APP_NAME} API",
    description=(
        "Learning, collaboration, academic resources, "
        "quizzes, and machine learning for the "
        "Amrapali University community."
    ),
    version=APP_VERSION,
)


app.include_router(
    auth_router,
    prefix=API_PREFIX,
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
