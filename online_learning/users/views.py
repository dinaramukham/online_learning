from django.contrib.auth.hashers import make_password
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Payment, Subscription, User
from .serializers import PaymentSerializer, MyTokenObtainPairSerializer, SubscriptionSerializer, UserSerializer
from .services import create_stripe_price, create_stripe_session, create_stripe_product
from rest_framework import routers

router = routers.SimpleRouter()


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        password = make_password(serializer.validated_data['password'])
        serializer.save(password=password)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Payment.objects.all()
    search_fields = ['lesson', 'courses', 'method_pay']
    ordering_fields = ['date_payment']


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated, ]
    queryset = Payment.objects.all()

    def perform_create(self, serializer):
        payment_serializer = serializer.save()
        stripe_product_id = create_stripe_product(payment_serializer.courses)
        stripe_price_id = create_stripe_price(stripe_product_id, payment_serializer.money)
        payment_serializer.link = create_stripe_session(stripe_price_id)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()


class SubscriptionListAPIView(generics.ListAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()
    search_fields = ['user', 'courses']
    ordering_fields = ['user', 'courses']


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]
    queryset = Subscription.objects.all()