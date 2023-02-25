from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import RegisterSerializer

# Create your views here.


# 회원가입 뷰
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
