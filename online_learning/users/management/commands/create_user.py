from django import db
from django.core.management import BaseCommand
from rest_framework.generics import get_object_or_404
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user=User.objects.create(
            email='user@gmail.com',
            first_name='Admin',
            last_name='Admin',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('etoyaadmin')
        user.save()

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcwODUxNzc3NSwiaWF0IjoxNzA4NDMxMzc1LCJqdGkiOiI4MDE4OGYyNTliNjQ0Mjc1YTA0OTE3NGY0YTQ1NzNiZiIsInVzZXJfaWQiOjl9.QnXsmw9AWm_I0w1ONcpq5tvxRfz0vKrkp_3iKetmclM