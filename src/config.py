from pydantic_settings import BaseSettings, SettingsConfigDict


class _Secrets(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")


class Settings(BaseSettings):
    secrets: _Secrets


settings = Settings()   # type: ignore
    