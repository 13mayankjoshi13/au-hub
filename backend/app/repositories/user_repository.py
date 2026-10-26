
from typing import Any

from backend.app.db.connection import get_db_connection


def get_user_by_email(email: str) -> dict[str, Any] | None:
    """Return a user by email, or None if no user exists."""
    connection = get_db_connection()

    try:
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                SELECT id, full_name, email, password_hash,
                       role, is_active, created_at, updated_at
                FROM users
                WHERE email = %s
                LIMIT 1
                """,
                (email,),
            )

            return cursor.fetchone()

        finally:
            cursor.close()

    finally:
        connection.close()


def create_user(
    full_name: str,
    email: str,
    password_hash: str,
) -> dict[str, Any]:
    """Create a user and return the public user fields."""
    connection = get_db_connection()

    try:
        cursor = connection.cursor(dictionary=True)

        try:
            cursor.execute(
                """
                INSERT INTO users (full_name, email, password_hash)
                VALUES (%s, %s, %s)
                """,
                (full_name, email, password_hash),
            )

            user_id = cursor.lastrowid
            connection.commit()

            cursor.execute(
                """
                SELECT id, full_name, email, role,
                       is_active, created_at, updated_at
                FROM users
                WHERE id = %s
                """,
                (user_id,),
            )

            user = cursor.fetchone()

            if user is None:
                raise RuntimeError(
                    "User was inserted but could not be retrieved."
                )

            return user

        except Exception:
            connection.rollback()
            raise

        finally:
            cursor.close()

    finally:
        connection.close()
