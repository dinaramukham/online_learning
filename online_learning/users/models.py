from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.IntegerField()
    city = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='media/avatar/')
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    courses = models.OneToOneField('Courses', on_delete=models.CASCADE, null=True, blank=True)
    lesson = models.OneToOneField('Lesson', on_delete=models.CASCADE, null=True, blank=True)
    method_pay = models.CharField(max_length=15, choices=(('cash', 'наличными'), ('card', 'картой')))
    date_payment = models.DateField()
    money = models.IntegerField()
