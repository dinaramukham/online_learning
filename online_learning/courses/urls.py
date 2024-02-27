from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import CoursesConfig
from . import views

app_name = CoursesConfig.name

router = DefaultRouter()
router.register('Courses', views.CoursesViewSet, basename='Courses')

urlpatterns = [
                  path('lesson/create/', views.LessonCreateAPIView.as_view(), name='lesson_create'),
                  path('lesson/list/', views.LessonListAPIView.as_view(), name='lesson_list'),
                  path('lesson/retrieve/<int:pk>/', views.LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
                  path('lesson/update/<int:pk>/', views.LessonUpdateAPIView.as_view(), name='lesson_update'),
                  path('lesson/delete/<int:pk>/', views.LessonDestroyAPIView.as_view(), name='lesson_destroy'),

                  path('courses/create/', views.CoursesCreateAPIView.as_view(), name='courses_create'),
                  path('courses/list/', views.CoursesListAPIView.as_view(), name='courses_list'),
                  path('courses/retrieve/<int:pk>/', views.CoursesRetrieveAPIView.as_view(), name='courses_retrieve'),
                  path('courses/update/<int:pk>/', views.CoursesUpdateAPIView.as_view(), name='courses_update'),
                  path('courses/delete/<int:pk>/', views.CoursesDestroyAPIView.as_view(), name='courses_destroy'),

                  path('subscription/', views.CoursesCreateSubscriptionAPIView.as_view(), name='subscription'),
              ] + router.urls
