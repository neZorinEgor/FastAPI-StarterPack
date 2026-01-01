from fastapi import APIRouter, Request, Response
from prometheus_client import REGISTRY
from prometheus_client.openmetrics.exposition import (
    CONTENT_TYPE_LATEST,
    generate_latest,
)

router = APIRouter(tags=["Prometheus metrics"])

@router.get("/metrics")
def metrics(request: Request) -> Response:
    return Response(
        content=generate_latest(REGISTRY), 
        headers={
            "Content-Type": CONTENT_TYPE_LATEST
        }
    )