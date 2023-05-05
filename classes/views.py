from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .permissions import CustomReadOnly
from .models import Class
from users.models import Profile
from .serializers import ClassSerializer, ClassCreateSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    permission_classes = [CustomReadOnly]
    filterset_fields = ['instructor', 'student', 'recommend']

    def get_serializer_class(self):
        if self.action == 'list' or 'retrieve':
            return ClassSerializer
        return ClassCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(instructor=self.request.user, profile=profile)


class RecommendView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        recommend_class = get_object_or_404(Class, id=pk)

        if request.user in recommend_class.recommend.all():
            recommend_class.recommend.remove(request.user)
        else:
            recommend_class.recommend.add(request.user)

        return Response({'status': 'ok'})


class JoinView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        join_class = get_object_or_404(Class, id=pk)

        if request.user in join_class.student.all():
            join_class.student.remove(request.user)
        else:
            join_class.student.add(request.user)

        return Response({'status': 'ok'})
