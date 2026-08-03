import os

from dotenv import load_dotenv

load_dotenv()


class LLMConfig:
    """
    Read all LLM configuration from .env
    """

    PROVIDER = os.getenv(
        "LLM_PROVIDER",
        "ollama"
    )

    MODEL = os.getenv(
        "OLLAMA_MODEL",
        "qwen3:8b"
    )

    TEMPERATURE = float(
        os.getenv(
            "OLLAMA_TEMPERATURE",
            "0.2"
        )
    )

    BASE_URL = os.getenv(
        "OLLAMA_BASE_URL",
        "http://localhost:11434"
    )