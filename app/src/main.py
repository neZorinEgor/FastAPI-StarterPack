import datetime
import logging
from contextlib import asynccontextmanager

from botocore.exceptions import ClientError
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend

from src.cloud.router import router as cloud_storage_router
from src.cache import redis_client

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(_: FastAPI):
    FastAPICache.init(RedisBackend(redis_client), prefix="fastapi-cache")
    yield
    pass


app = FastAPI(
    title="FastAPI-Starter",
    lifespan=lifespan,
    description="`Skeleton value`.",
    docs_url="/docs",
    version="1.0.0"
)


@app.exception_handler(ClientError)
async def s3_handle_exception(request: Request, exception: ClientError):
    # TODO send message on sentry...
    logger.error("Unexpected error!", exc_info=exception)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={
            "timestamp": datetime.datetime.now(datetime.UTC).timestamp(),
            "message": "An unexpected scenario has occurred. We are already working on this problem."
        }
    )

# origins url's for CORS
origins = ["*"]

# cors middleware
app.add_middleware(
    CORSMiddleware, # noqa
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)
# app routers
app.include_router(cloud_storage_router)
