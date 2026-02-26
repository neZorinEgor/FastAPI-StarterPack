FROM python:3.12-slim AS builder

WORKDIR /build

RUN pip install --upgrade pip

COPY pyproject.toml .

RUN --mount=type=cache,target=/root/.cache/pip \ 
    pip wheel --wheel-dir=/wheels -e .

FROM python:3.12-slim

RUN apt-get update && apt-get install -y curl

WORKDIR /ads-helper

COPY pyproject.toml .

RUN --mount=type=bind,from=builder,source=/wheels,target=/wheels \
    pip install --no-index --find-links=/wheels --no-cache-dir -e .

COPY . .

COPY docker-entrypoint.sh .

RUN chmod +x docker-entrypoint.sh

ENTRYPOINT [ "./docker-entrypoint.sh" ]