import datetime
import os
from io import BytesIO

from fastapi import APIRouter, UploadFile
from fastapi.responses import StreamingResponse

from src.config import settings
from src.filestorage import s3_client


router = APIRouter(prefix="/cloud", tags=["CloudStorage"])


@router.post(path="/upload")
async def upload_file(file: UploadFile):
    filename = file.filename
    # validate exist key in bucket
    if await s3_client.get_file(bucket=settings.MINIO_BUCKET_NAME, key=file.filename):
        file_name, file_extension = os.path.splitext(filename)
        file_name = file_name + "_" + str(int(datetime.datetime.now(datetime.UTC).timestamp()))
        filename = file_name + file_extension
    # upload file
    await s3_client.upload_file(
        bucket=settings.MINIO_BUCKET_NAME,
        key=filename,
        file=await file.read()
    )


@router.get(path="/{filename}")
async def download_file(filename: str):
    file = await s3_client.get_file(bucket=settings.MINIO_BUCKET_NAME, key=filename)
    return StreamingResponse(
        content=BytesIO(file),
    )
