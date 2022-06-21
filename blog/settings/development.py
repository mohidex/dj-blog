import imp
import os

from .base import *

# Database

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME"),
        "USER": os.environ("DATABASE_USER"),
        "PASSWORD": os.environ("DATABASE_PASSWORD"),
        "HOST": os.environ("DATABASE_HOST"),
        "PORT": os.environ("DATABASE_PORT"),
    }
}
