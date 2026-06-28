import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def require_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")

    return value


AZURE_OPENAI_ENDPOINT = require_env("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_API_KEY = require_env("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_EMBEDDING_MODEL = require_env("AZURE_OPENAI_EMBEDDING_MODEL")
AZURE_SEARCH_ENDPOINT = require_env("AZURE_SEARCH_ENDPOINT")
AZURE_SEARCH_KEY = require_env("AZURE_SEARCH_KEY")
AZURE_SEARCH_INDEX = require_env("AZURE_SEARCH_INDEX")
AZURE_OPENAI_API_VERSION = require_env("AZURE_OPENAI_API_VERSION")