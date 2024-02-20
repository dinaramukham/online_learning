from django.shortcuts import render
from requests import Response

from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Lesson, Courses
from .paginators import MyPageNumberPagination
from .serliazers import CoursesSerializer, LessonSerializer
from users.models import Subscription
from users.permission import ModeratorPermissionsClass, IsOwnerPermissionsClass




# Create your views here.
class CoursesCreateAPIView(generics.CreateAPIView ):
    permission_classes = [IsAuthenticated]
    serializers_class=CoursesSerializer

class CoursesRetrieveAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = CoursesSerializer
    queryset = Courses.objects.all()
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
    pagination_class=MyPageNumberPagination
class CoursesDestroyAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()

class CoursesPostAPIView(APIView):
    permission_classes = [IsAuthenticated]
    queryset = Courses.objects.all()
    def post(self, *args, **kwargs):
        user= self.requests.user
        course_id=self.reqests.data['id']
        course_item=get_object_or_404(Subscription, id=course_id )
        subs_item=Subscription.objects.get(user=user, courses=course_item)
        if subs_item.exists():
            subs_item.delete()
            subs_item.save()
            message = 'подписка удалена'
        else:
            Subscription.objects.create(user=user, courses=course_item)
            message = 'подписка добавлена'
        return Response({"message": message})

#             Lesson
class LessonCreateAPIView(generics.CreateAPIView ):
    permission_classes = [IsAuthenticated]
    serializers_class=LessonSerializer

class LessonListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated, ModeratorPermissionsClass | IsOwnerPermissionsClass]
    serializers_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class=MyPageNumberPagination

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