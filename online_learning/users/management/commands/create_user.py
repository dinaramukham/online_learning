from django import db
from django.core.management import BaseCommand
from rest_framework.generics import get_object_or_404
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='zakalibe@gmail.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('etoyaadmin')
        user.save()
# pbkdf2_sha256$600000$c0zF1JUxYB28Abv2Ft2nk8$4cjLM1teBEvlfq25q8OvMvURQ6gZz8Et7NwyFePkbrg=