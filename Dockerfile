FROM python:3.11-alpine3.18
LABEL maintainer="frankjlin16"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . ./app

WORKDIR /app

RUN pip install --upgrade pip
RUN apk add --no-cache --virtual build-deps gcc musl-dev pkgconf mariadb-dev && \
    apk add --no-cache mariadb-connector-c-dev && \
    apk add --no-cache mysql-client && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps
