import datetime

from fastapi import APIRouter, Response, status

from src.schemas.common import HTTPResponseStatus
from src.schemas.healthcheck import AliveHTTPResponse

router = APIRouter(prefix="/healthcheck", tags=["Healthcheck"])


@router.get(
    path="/alive", 
    response_model=AliveHTTPResponse,
    status_code=status.HTTP_200_OK
)
def liveness() -> AliveHTTPResponse:
    return AliveHTTPResponse(
        status=HTTPResponseStatus.SUCCESS,
        message="alive", 
        timestamp=datetime.datetime.now(datetime.UTC).timestamp()
    )


@router.get("/ready")
def readiness():
    pass