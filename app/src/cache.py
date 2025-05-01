from redis import asyncio as aioredis

from src.config import settings


redis_client = aioredis.from_url(settings.redis_url, db=0)
