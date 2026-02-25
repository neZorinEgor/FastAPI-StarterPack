from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__name__).resolve().parent


class _CorsConfig(BaseModel):
    ORIGINS: list[str]
    METHODS: list[str]
    HEADERS: list[str]
    CREDENTIALS: bool


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="PROJECT_PREFIX__",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_file=".env",
    )

    cors: _CorsConfig


settings = Settings()
