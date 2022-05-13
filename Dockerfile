# syntax=docker/dockerfile:1
FROM python:3
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py migrate
RUN python manage.py makemigrations
CMD [ "python", "manage.py", "runserver"]
EXPOSE 8000
