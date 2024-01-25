from django.urls import path
from rest_framework.routers import DefaultRouter

from online_learning.courses.apps import CoursesConfig
from online_learning.courses.views import CoursesViewSet

app_name= CoursesConfig.name

router=DefaultRouter()
router.register(r'Courses', CoursesViewSet, basename='Courses')

urlpatterns = [
    path(''),
]+ router.urls