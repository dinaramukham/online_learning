from django.db import models


# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photo/')
    content = models.TextField()

    def __str__(self):
        return self.title


class Lesson(models.Model):
    courses = models.ForeignKey('Courses', on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/photo/')
    content = models.TextField()
    link_video = models.TextField()

    def __str__(self):
        return self.title
