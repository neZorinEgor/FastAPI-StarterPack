import asyncio

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.lifespan import lifespan
from src.middleware.metrics import PrometheusMetricsMiddleware
from src.routers.healthcheck import router as healthcheck_router
from src.routers.metrics import router as metrics_router


async def main():
    app = FastAPI(lifespan=lifespan)
    # routers
    app.include_router(metrics_router)
    app.include_router(healthcheck_router)
    # middleware list
    app.add_middleware(PrometheusMetricsMiddleware, app_name="app")
    app.add_middleware(
        CORSMiddleware, 
        allow_credentials=True,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # Server settings
    server_config = uvicorn.Config(app, host="0.0.0.0", port=8000, workers=5)
    server = uvicorn.Server(config=server_config)
    await server.serve()


if __name__ == "__main__":
    asyncio.run(main=main())