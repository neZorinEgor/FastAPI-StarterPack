from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend


from app.src.config import settings

import logging
from redis import asyncio as aioredis
from contextlib import asynccontextmanager

logging.basicConfig(level=logging.INFO)


@asynccontextmanager
async def lifespan(_: FastAPI):
    redis = aioredis.from_url(settings.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield
    pass


app = FastAPI(
    title="FastAPI-Starter",
    lifespan=lifespan,
    description="...",
    docs_url="/docs",
    version="1.0.0"
)

# Origins url's for CORS
origins = ["*"]


# Cors middleware
app.add_middleware(
    CORSMiddleware, # noqa
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
