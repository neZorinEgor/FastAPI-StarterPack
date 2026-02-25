from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.project.presentation.api.lifespan import lifespan
from src.project.presentation.api.middleware.metrics import PrometheusMetricsMiddleware
from src.project.presentation.api.routers.healthcheck import (
    router as healthcheck_router,
)
from src.project.presentation.api.routers.metrics import router as metrics_router
from src.project.setup import settings


def make_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(healthcheck_router)
    app.include_router(metrics_router)
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
