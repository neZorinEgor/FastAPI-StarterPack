import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from src.project.presentation.api.lifespan import lifespan
from src.project.presentation.api.middleware.metrics import PrometheusMetricsMiddleware
from src.project.presentation.api.routers.healthcheck import (
    router as healthcheck_router,
)
from src.project.presentation.api.routers.metrics import router as metrics_router
from src.project.presentation.api.routers.swagger import router as swagger_router
from src.project.setup import settings
from src.project.setup.config import STATIC_PATH


def make_app() -> FastAPI:
    app = FastAPI(
        title="Project",
        version="v0.1.0",
        lifespan=lifespan,
        docs_url=None,  # include in swagger router
        redoc_url=None,  # include in swagger router
    )
    app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
    app.include_router(healthcheck_router)
    app.include_router(metrics_router)
    app.include_router(swagger_router)
    app.add_middleware(PrometheusMetricsMiddleware, app_name="project")
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors.ORIGINS,
        allow_methods=settings.cors.METHODS,
        allow_headers=settings.cors.HEADERS,
        allow_credentials=settings.cors.CREDENTIALS,
    )
    return app


app = make_app()

log_config = uvicorn.config.LOGGING_CONFIG
log_config["formatters"]["access"][
    "fmt"
] = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] - %(message)s"
uvicorn.run(app, log_config=log_config, host="0.0.0.0", port=8000)
