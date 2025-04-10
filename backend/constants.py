import os
from backend.env import config
from functools import lru_cache


def convert_to_list(value: str) -> list[str]:
    return [item.strip() for item in value.split(',')]

class Constants(object):
    DJANGO_DEBUG: bool = config("DJANGO_DEBUG",cast=bool)
    DJANGO_ALLOWED_HOSTS: list[str] = convert_to_list(
        value=config("DJANGO_ALLOWED_HOSTS", cast=str)
    )
    DJANGO_SECRET_KEY: str = config("DJANGO_SECRET_KEY", cast=str)
    USE_POSTGRES: bool = config("USE_POSTGRES", cast=bool, default=False)
    DATABASE_URL: str = config("DATABASE_URL", cast=str)

    
@lru_cache
def get_constants() -> Constants:
    return Constants()
