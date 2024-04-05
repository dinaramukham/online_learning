from celery import shared_task
from django.core.mail import send_mail

from online_learning.settings import EMAIL_HOST_USER


@shared_task
def send_email_info(name_email, message):
    send_mail(
        "Обновление",
        message,
        EMAIL_HOST_USER,
        [name_email],
        fail_silently=False,
    )