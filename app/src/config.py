from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    # database
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    # filestorage
    MINIO_API_PORT: int
    MINIO_API_HOST: str
    MINIO_AWS_ACCESS_KEY_ID: str
    MINIO_AWS_SECRET_ACCESS_KEY: str
    MINIO_BUCKET_NAME: str
    # cache | broker
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def postgres_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    @property
    def s3_url(self) -> str:
        return f"http://{settings.MINIO_API_HOST}:{settings.MINIO_API_PORT}"

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings() # noqa
