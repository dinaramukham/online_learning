from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .models import Lesson, Courses
from .serliazers import CoursesSerializer, LessonSerializer
from users.permission import ModeratorPermissionsClass, IsOwnerPermissionsClass



# Create your views here.
class CoursesCreateAPIView(generics.CreateAPIView ):
    permission_classes = [IsAuthenticated]
    serializers_class=CoursesSerializer

class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializer_class=CoursesSerializer
    queryset = Courses.objects.all()

class CoursesUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = CoursesSerializer
    queryset = Courses.objects.all()

class CoursesListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = CoursesSerializer
    queryset = Courses.objects.all()

class CoursesDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()



class LessonCreateAPIView(generics.CreateAPIView ):
    permission_classes = [IsAuthenticated]
    serializers_class=LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()

class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()