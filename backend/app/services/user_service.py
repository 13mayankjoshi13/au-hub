
from mysql.connector import IntegrityError
from pwdlib import PasswordHash

from backend.app.repositories.user_repository import (
    create_user,
    get_user_by_email,
)
from backend.app.schemas.user import UserCreate, UserResponse


password_hasher = PasswordHash.recommended()


class EmailAlreadyRegisteredError(Exception):
    """Raised when an email address is already registered."""


class InvalidCredentialsError(Exception):
    """Raised when login credentials are invalid."""


def hash_password(password: str) -> str:
    """Convert a plain-text password into a secure password hash."""
    return password_hasher.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    """Check whether a plain-text password matches its stored hash."""
    return password_hasher.verify(plain_password, hashed_password)


def register_user(user_data: UserCreate) -> UserResponse:
    """Validate registration rules and create a new user."""
    existing_user = get_user_by_email(str(user_data.email))

    if existing_user is not None:
        raise EmailAlreadyRegisteredError(
            "An account with this email already exists."
        )

    hashed_password = hash_password(user_data.password)

    try:
        created_user = create_user(
            full_name=user_data.full_name,
            email=str(user_data.email),
            password_hash=hashed_password,
        )

    except IntegrityError as error:
        if error.errno == 1062:
            raise EmailAlreadyRegisteredError(
                "An account with this email already exists."
            ) from error

        raise

    return UserResponse.model_validate(created_user)


def authenticate_user(
    email: str,
    password: str,
) -> UserResponse:
    """Verify login credentials and return public user details."""
    user = get_user_by_email(email)

    if user is None:
        raise InvalidCredentialsError("Invalid email or password.")

    if not user["is_active"]:
        raise InvalidCredentialsError("Invalid email or password.")

    if not verify_password(password, user["password_hash"]):
        raise InvalidCredentialsError("Invalid email or password.")

    return UserResponse.model_validate(user)
