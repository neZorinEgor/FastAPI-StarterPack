from enum import Enum

from pydantic import BaseModel


class HTTPResponseStatus(str, Enum):
    SUCCESS = "success"
    ERROR = "error"


class BaseHTTPResponse(BaseModel):
    status: str
    message: str
    timestamp: float