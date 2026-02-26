from fastapi import APIRouter, Response
from prometheus_client import REGISTRY
from prometheus_client.openmetrics.exposition import (
    CONTENT_TYPE_LATEST,
    generate_latest,
)

router = APIRouter(prefix="/metrics", tags=["Prometheus"])


@router.get("")
def metrics() -> Response:
    return Response(
        content=generate_latest(REGISTRY), headers={"Content-Type": CONTENT_TYPE_LATEST}
    )
