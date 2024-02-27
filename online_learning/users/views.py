from django.contrib.auth.models import Group
# /Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/django/contrib/auth/models.py
from rest_framework import generics, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Payment, Subscription, User
from .serializers import PaymentSerializer, MyTokenObtainPairSerializer, SubscriptionSerializer, UserSerializer

from rest_framework import routers

router = routers.SimpleRouter()


# Create your views here.
class MyTokenObtainPairView(TokenObtainPairSerializer):
    serializer_class = MyTokenObtainPairSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(detail=True, methods=['post'])
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data['password'])
            user.save()
            return Response({'status': 'password set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


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
