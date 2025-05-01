from typing import Annotated

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase,  registry
from sqlalchemy import String

from src.config import settings

# async engin
engine = create_async_engine(
    url=settings.postgres_url,
    echo=False,
)

# async session factory
session_factory = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
)

# varchar types
str_50 = Annotated[str, 50]
str_128 = Annotated[str, 128]
str_255 = Annotated[str, 255]


# base class for all application sql model
class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str_50: String(50),
            str_128: String(128),
            str_255: String(255)
        }
    )
