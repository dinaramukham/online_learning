from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .apps import UsersConfig
from .views import UserViewSet, PaymentCreateAPIView, PaymentListAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')


name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view())
    path('payment_create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),

]+ router.urls
