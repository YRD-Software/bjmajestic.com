# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /usr/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate