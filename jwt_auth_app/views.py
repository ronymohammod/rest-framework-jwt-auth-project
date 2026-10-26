from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *

from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import LoginSerializer

from rest_framework_simplejwt.views import TokenBlacklistView

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from django.contrib.auth import get_user_model

User = get_user_model()
from rest_framework.permissions import IsAuthenticated, IsAdminUser








class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = []

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response(
            {
                "success": True,
                "message": "User registered successfully",
                "data": UserSerializer(user).data,
            },
            status=status.HTTP_201_CREATED,
        )




# from rest_framework_simplejwt.views import TokenObtainPairView
# from .serializers import LoginSerializer


class LoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return Response({
             "success": True,
             "message": "Login successful.",
             "data": response.data,
        },
        status = status.HTTP_200_OK)



# from rest_framework_simplejwt.views import TokenBlacklistView

class LogoutView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        response.data = {
            "success": True,
            "message": "Logout successful.",
            "data": None,
        }

        return response  





# from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "success": True,
            "message": "Profile retrieved successfully.",
            "data": UserSerializer(request.user).data,
        })        



class UserList(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]




# from rest_framework_simplejwt.views import TokenBlacklistView

class LogoutView(TokenBlacklistView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        return response ({
            "success": True,
            "message": "Logout successful.",
            "data": None,
        },
        )
  



