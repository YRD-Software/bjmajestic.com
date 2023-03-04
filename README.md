
# Majestic Web

## Developer's Guide

**Required:**
- Pipenv
- Pyenv

### Local development
`pipenv install`

---

## Deployment

### Environment variables
```properties
# Django Settings variables
DJANGO_DEBUG=<True/False>
SECRET_KEY=<Django's secrete key>
DJANGO_ALLOWED_HOSTS=<IP address or domain>

# Storage environment variables
USE_OSS=<True/False>
OSS_ACCESS_KEY_ID=<key id>
OSS_ACCESS_KEY_SECRET=<secret key>
OSS_BUCKET_NAME=<bucket name>
OSS_ENDPOINT=<host or endpoint>

# Contact Us email environment variables
USE_SMTP=<True/False>
DEFAULT_FROM_EMAIL=<default from email>
DEFAULT_TO_EMAIL=<default to email>
EMAIL_HOST=<host>
EMAIL_PORT=<port: 80 or 443 (SSL)>
EMAIL_HOST_USER=<host username>
EMAIL_HOST_PASSWORD=<host password>

# MySQL Database
USE_MYSQL=<True/False>
DATABASE_NAME=<database name>
DATABASE_USER=<database username>
DATABASE_PASSWORD=<database password>
DATABASE_HOST=<Database host>
DATABASE_PORT=<MYSQL port: default is 3306>

# Superuser initialization environment variables (python manage.py initadmin)
SUPERUSER_USERNAME=<username>
SUPERUSER_PASSWORD=<password>
```

> This project uses the Gunicorn and Nginx server tech stack