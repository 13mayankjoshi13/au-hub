
import os

APP_NAME = "AU Hub"
APP_VERSION = "0.1.0"
API_PREFIX = "/api/v1"

DB_HOST = os.getenv("AU_HUB_DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("AU_HUB_DB_PORT", "3306"))
DB_USER = os.getenv("AU_HUB_DB_USER", "root")
DB_PASSWORD = os.getenv("AU_HUB_DB_PASSWORD", "")
DB_NAME = os.getenv("AU_HUB_DB_NAME", "au_hub")
