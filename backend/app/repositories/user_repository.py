
from typing import Any

from backend.app.db.connection import get_db_connection


def get_user_by_email(email: str) -> dict[str, Any] | None:
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
