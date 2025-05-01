from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    APP_PORT: int
    APP_HOST: str
    # Database
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    # Filestorage
    MINIO_API_PORT: int
    MINIO_API_HOST: str
    MINIO_WEB_UI_PORT: int
    MINIO_ROOT_USER: str
    MINIO_ROOT_PASSWORD: str
    MINIO_AWS_ACCESS_KEY_ID: str
    MINIO_AWS_SECRET_ACCESS_KEY: str
    MINIO_BUCKET_NAME: str
    # Cache | broker
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def s3_endpoint_url(self) -> str:
        return f"http://{settings.S3_HOST}:{settings.GATEWAY_LISTEN}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # noqa
