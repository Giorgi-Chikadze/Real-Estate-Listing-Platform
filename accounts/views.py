from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import AgentProfile
from django.contrib.auth import get_user_model
from accounts.serializers import RegisterSerializer, UserSerializer, BecomeAgentSerializer
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


class RegisterView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class UserListDetailViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class BecomeAgentView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = AgentProfile.objects.all()
    serializer_class = BecomeAgentSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)


        if AgentProfile.objects.filter(user=request.user).exists():
            return Response({"error":"You are already an Agent"}, status = status.HTTP_400_BAD_REQUEST)
        
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(
            {"message":"You have successfully become an agent, you can now list properties for sale"}, status=status.HTTP_201_CREATED
        )
        


