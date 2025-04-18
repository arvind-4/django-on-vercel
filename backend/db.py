"""Configuration for the database."""

import dj_database_url
from django.conf import settings

from backend.constants import get_constants

constants = get_constants()

BASE_DIR = settings.BASE_DIR

DATABASES = {}

if constants.DJANGO_DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        },
    }
else:
    DATABASES["default"] = dj_database_url.config()
