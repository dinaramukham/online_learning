from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
]+ router.urls
