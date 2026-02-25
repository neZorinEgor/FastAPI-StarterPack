from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/healthcheck", tags=["Healthcheck"])


@router.get(
    path="/alive",
    status_code=status.HTTP_200_OK,
)
async def alive() -> int:
    return 0


@router.get("/ready")
async def ready():
    raise HTTPException(
        detail="Not implemented", status_code=status.HTTP_501_NOT_IMPLEMENTED
    )
