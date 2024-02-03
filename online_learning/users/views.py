from django.shortcuts import render
from rest_framework import generics

from .models import Payment
from .serliazers import PaymentSerializer


# Create your views here.
class PaymentListAPIView(generics.ListAPIView):
    serializers_class = PaymentSerializer
    queryset = Payment.objects.all()
    search_fields=['lesson', 'courses', 'method_pay']
    ordering_fields = ['date_payment']