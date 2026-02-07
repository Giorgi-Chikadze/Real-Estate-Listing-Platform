from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import get_user_model
from accounts.serializers import RegisterSerializer, UserSerializer

User = get_user_model()

# Create your views here

class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class UserListDetailViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

