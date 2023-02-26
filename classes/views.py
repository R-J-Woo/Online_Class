from django.shortcuts import render
from rest_framework import viewsets
from .permissions import CustomReadOnly
from .models import Class
from users.models import Profile
from .serializers import ClassSerializer, ClassCreateSerializer

# Create your views here.


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    permission_classes = [CustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ClassSerializer
        return ClassCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.requset.user)
        serializer.save(instructor=self.request.user, profile=profile)
