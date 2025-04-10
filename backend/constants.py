"""Constants for the entire application."""

from functools import lru_cache

from backend.env import config


def convert_to_list(value: str) -> list[str]:
    """Convert a comma-separated string to a list of strings."""
    return [item.strip() for item in value.split(",")]


class Constants:
    """Constants for the application."""

    DJANGO_DEBUG: bool = config("DJANGO_DEBUG", cast=bool)
    DJANGO_ALLOWED_HOSTS: list[str] = convert_to_list(
        value=config("DJANGO_ALLOWED_HOSTS", cast=str),
    )
    DJANGO_SECRET_KEY: str = config("DJANGO_SECRET_KEY", cast=str)
    USE_POSTGRES: bool = config("USE_POSTGRES", cast=bool, default=False)
    DATABASE_URL: str = config("DATABASE_URL", cast=str)


@lru_cache
def get_constants() -> Constants:
    """Get the constants for the application."""
    return Constants()
