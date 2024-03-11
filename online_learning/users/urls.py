from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

from .apps import UsersConfig
from .views import UserViewSet, PaymentCreateAPIView, PaymentListAPIView, SubscriptionCreateAPIView, \
    SubscriptionListAPIView, SubscriptionDestroyAPIView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

app_name = UsersConfig.name

urlpatterns = [
                  path('token/', TokenObtainPairView.as_view()),
                  path('token/refresh/', TokenRefreshView.as_view()),

                  path('payment_create/', PaymentCreateAPIView.as_view(), name='payment_create'),
                  path('payment_list/', PaymentListAPIView.as_view(), name='payment_list'),

                  path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
                  path('subscription_list/', SubscriptionListAPIView.as_view(), name='subscription_list'),
                  path('subscription_destroy/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),
              ] + router.urls
