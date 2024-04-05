from django.db import models


# Create your models here.
class Courses(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photo/', null=True, blank=True, )
    content = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.DO_NOTHING, null=True, blank=True)
    courses = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, null=True, blank=True)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photo/', null=True, blank=True, )
    content = models.TextField()
    link_video = models.TextField(null=True, blank=True, )

    def __str__(self):
        return self.title