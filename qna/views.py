from django.shortcuts import render
from rest_framework import viewsets
from .models import Question, Answer
from .serializers import QuestionSerializer, QuestionCreateSerializer, AnswerSerializer, AnswerCreateSerializer
from classes.permissions import CustomReadOnly
from users.models import Profile
from .permissions import QuestionCustomReadOnly, AnswerCustomReadOnly

# Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    permission_classes = [QuestionCustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retreive':
            return QuestionSerializer
        return QuestionCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(questioner=self.request.user, profile=profile)


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    permission_classes = [AnswerCustomReadOnly]

    def get_serializer_class(self):
        if self.action == 'list' or 'retreive':
            return AnswerSerializer
        return AnswerCreateSerializer

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(answerer=self.request.user, profile=profile)
