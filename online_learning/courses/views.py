from django.shortcuts import render
from rest_framework import viewsets

from online_learning.courses.models import Lesson
from online_learning.courses.serliazers import LessonSerializer


# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class=LessonSerializer
    queryset = Lesson.objects.all()