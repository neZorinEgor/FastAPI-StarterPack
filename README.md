# FastAPI-StarterPack
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" title="FastAPI" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" title="FastAPI" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" title="FastAPI" width="40" height="40"/>&nbsp;
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" title="FastAPI" width="40" height="40"/>&nbsp;

> Everything you need to create a `production ready` application on FastAPI.

Feature:
1. DB configuration: `Postgres + SQLAlchemy + Alembic`
2. Filestorage: `AWS-S3`
3. Broker/Cache: `Celery + Redis`

The presence of `postgresql`, `redis` and `s3` is simulated in `docker-compose`.

###  Usefulness's:
1. Creating and launching migrations:
```bash
alembic revision --autogenerate -m "<migration message>"
alembic upgrade head
```
2. Setting up models for migration in [env.py](app/alembic/env.py)
```bash
# add your model's MetaData object here
from src.database import Base
# Your models here ↓
# from src.<your_service_name>.model import SomeModel

target_metadata = Base.metadata
```
3. Generation of `RSA` keys for JWT: 
```bash
# Generate an RSA private key of size 2048
openssl genrsa -out jwt-private.pem 2048
# Extract a public key from a key pair that can be used in a certificate
openssl rsa -in jwt-private.pem -outform PEM -pubout -out jwt-public.pem
```

4. Cache connections to `get` routers:
```python
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
@cache(expire=60)   # <--- Obligatory after the router decorator
async def index():
    return dict(hello="world")
```
5. Local dev start up:
```bash
docker compose up
alembic upgrade head; uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

