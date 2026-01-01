FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000