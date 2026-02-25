from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.project.setup.app_logging import init_logging


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator:
    init_logging()
    yield
