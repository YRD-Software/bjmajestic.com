"""Create superuser if not exist."""
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.conf import settings

class Command(BaseCommand):
    """Create superuser if not exist."""

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            username = settings.SUPERUSER_USERNAME
            password = settings.SUPERUSER_PASSWORD
            print('Creating superuser...')
            admin = User.objects.create_superuser(email='', username=username, password=password)
            admin.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully.'))
        else:
            print('Superuser initialization skipped. (User already exist)')
