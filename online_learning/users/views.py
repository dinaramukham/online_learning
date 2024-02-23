from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Payment, Subscription
from .serializers import PaymentSerializer, MyTokenObtainPairSerializer, SubscriptionSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # ModeratorPermissionsClass | IsOwnerPermissionsClass]
    queryset = Payment.objects.all()
    search_fields = ['lesson', 'courses', 'method_pay']
    ordering_fields = ['date_payment']


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]  # ModeratorPermissionsClass | IsOwnerPermissionsClass]
    queryset = Subscription.objects.all()
    search_fields = ['user', 'courses']
    ordering_fields = ['user', 'courses']
