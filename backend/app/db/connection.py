
import mysql.connector
from mysql.connector import Error

from backend.app.core.config import (
    DB_HOST,
    DB_PORT,
    DB_USER,
    DB_PASSWORD,
    DB_NAME,
)


def get_db_connection():
    """Create and return a MySQL database connection."""
    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            connection_timeout=5,
        )
        return connection

    except Error:
        raise


def check_database_connection() -> bool:
    """Return True if a database query succeeds."""
    connection = None

    try:
        connection = get_db_connection()

        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        return result == (1,)

    except Error:
        return False

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
