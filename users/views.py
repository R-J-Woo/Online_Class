from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerailizer, ProfileSerializer
from .models import Profile
from .permissions import CustomReadOnly

# Create your views here.


# 회원가입 뷰
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerailizer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data  # validate()의 리턴값인 token을 받아옴
        return Response({"token": token.key}, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
    def get(self, request):
        response = Response({"message": "로그아웃 되었습니다."},
                            status=status.HTTP_202_ACCEPTED)
        response.delete_cookie('token')
        return response


class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [CustomReadOnly]
