from django.utils import timezone

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    # objects = UserManager()
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35, null=True, blank=True, )
    city = models.CharField(max_length=50, null=True, blank=True, )
    avatar = models.ImageField(null=True, blank=True, upload_to='media/')
    last_login = models.DateField(null=True, blank=True, default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    courses = models.OneToOneField('courses.Courses', on_delete=models.DO_NOTHING, null=True, blank=True)
    lesson = models.OneToOneField('courses.Lesson', on_delete=models.DO_NOTHING, null=True, blank=True)
    method_pay = models.CharField(max_length=15, choices=(('cash', 'наличными'), ('card', 'картой')))
    date_payment = models.DateField(default=timezone.now, null=True, blank=True)
    money = models.IntegerField()
    link = models.URLField(max_length=400, verbose_name='Ссылка на оплату', null=True, blank=True)


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    courses = models.ForeignKey('courses.Courses', on_delete=models.DO_NOTHING)
