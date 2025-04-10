"""Configure environment variables for the application."""

import pathlib
from functools import lru_cache

from decouple import Config, RepositoryEnv
from decouple import config as config_default

BASE_DIR = pathlib.Path(__file__).parent.parent

ENV_PATH = BASE_DIR / ".env"


@lru_cache
def get_config() -> Config:
    """Get the configuration from the .env file if it exists."""
    if ENV_PATH.exists():
        return Config(RepositoryEnv(ENV_PATH))
    return config_default


config = get_config()
