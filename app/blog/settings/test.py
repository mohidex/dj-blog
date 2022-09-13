from pathlib import Path

from .base import *

BASE_DIR = Path(__file__).resolve().parent.parent


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
