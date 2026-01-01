from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.config import settings
from src.logger import init_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_logger(config_path=settings.paths.PATH_TO_LOGGER_CONFIG)
    yield