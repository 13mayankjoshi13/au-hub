
from fastapi import APIRouter, HTTPException, status

from backend.app.schemas.user import UserCreate, UserResponse
from backend.app.services.user_service import (
    EmailAlreadyRegisteredError,
    register_user,
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(user_data: UserCreate) -> UserResponse:
    """Register a new AU Hub user."""
    try:
        return register_user(user_data)

    except EmailAlreadyRegisteredError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error
