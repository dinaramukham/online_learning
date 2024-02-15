
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from .apps import UsersConfig

name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenObtainPairView.as_view())
]