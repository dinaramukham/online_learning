from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone=models.IntegerField()
    city=models.CharField(max_length=50 )
    avatar=models.ImageField(upload_to='media/avatar/')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []