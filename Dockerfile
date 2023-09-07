FROM python:3.11-alpine3.18
LABEL maintainer="frankjlin16"

ENV PYTHONUNBUFFERED 1

COPY . ./app

WORKDIR /app

EXPOSE 8000

RUN apk add --no-cache --virtual build-deps gcc musl-dev pkgconf mariadb-dev && \
    apk add --no-cache mariadb-connector-c-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-deps

RUN python manage.py makemigrations && \
    python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


