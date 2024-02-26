from django.db.migrations import serializer
from django.shortcuts import render
from requests import Response

from rest_framework import viewsets, generics
from rest_framework.fields import SerializerMethodField
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from .models import Lesson, Courses
from .paginators import MyPageNumberPagination
from .permission import IsOwnerPermissionsClass, IsModer
from .serializers import CoursesSerializer, LessonSerializer
from users.models import Subscription



# Create your views here.
class CoursesCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CoursesSerializer

    def post(self, *args, **kwargs):
        user = self.requests.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Courses, id=course_id)
        if course_item == None:
            course_item.user=user
            course_item.save()
        return Response()


class CoursesRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsModer | IsOwnerPermissionsClass]
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class CoursesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsModer | IsOwnerPermissionsClass]
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class CoursesUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsModer | IsOwnerPermissionsClass]
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class CoursesListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    pagination_class = MyPageNumberPagination

#| IsOwnerPermissionsClass
class CoursesDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()


class CoursesCreateSubscriptionAPIView(APIView):
    """
    логика  подписки
    """
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()

    def post(self, *args, **kwargs):
        user = self.requests.user
        course_id = self.request.data.get('course_id')
        course_item = get_object_or_404(Courses, id=course_id)
        subs_item = Subscription.objects.filter(user=user, courses=course_item)
        if subs_item.exists():
            subs_item.delete()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, courses=course_item)
            message = 'подписка добавлена'
        return Response({"message": message})


#             Lesson
class LessonCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = MyPageNumberPagination


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsModer | IsOwnerPermissionsClass]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsModer | IsOwnerPermissionsClass]
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Lesson.objects.all()
