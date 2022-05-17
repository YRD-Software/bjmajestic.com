# syntax=docker/dockerfile:1
FROM python:3
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt