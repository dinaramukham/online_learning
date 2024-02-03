from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import Lesson, Courses
from .serliazers import CoursesSerializer, LessonSerializer


# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    serializer_class=CoursesSerializer
    queryset = Courses.objects.all()

class LessonCreateAPIView(generics.CreateAPIView ):
    serializers_class=LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()