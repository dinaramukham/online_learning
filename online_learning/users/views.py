from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Payment, Subscription
from .serliazers import PaymentSerializer, MyTokenObtainPairSerializer, SubscriptionSerializer


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


class PaymentListAPIView(generics.ListAPIView):
    serializers_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    search_fields = ['lesson', 'courses', 'method_pay']
    ordering_fields = ['date_payment']

class SubscriptionListAPIView(generics.ListAPIView):
    serializers_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    search_fields = ['user', 'courses']
    ordering_fields = ['user', 'courses']
