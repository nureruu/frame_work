
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer, ConfirmationSerializer, LoginSerializer, ConfirmSerializer
from rest_framework.authtoken.models import Token
from .models import User, ConfirmationCode
from rest_framework import status
from rest_framework.views import TokenObtainPairView
from rest_framework.views import TokenObtainPairSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Пользователь зарегистрирован. Проверьте код подтверждения."}, status=status.HTTP_201_CREATED)


class ConfirmUserView(APIView):
    def post(self, request):
        serializer = ConfirmationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        user.is_active = True
        user.save()
        ConfirmationCode.objects.filter(user=user).delete()
        return Response({"message": "Пользователь подтверждён."})


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    
class ConfirmUserView(APIView):
    def post(self, request):
        serializer = ConfirmSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail": "Пользователь успешно подтвержден."}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Login(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer