from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Question, Answer
from .serializers import QuestionSerializer, QuestionCreateSerializer, AnswerSerializer, AnswerCreateSerializer
from classes.permissions import CustomReadOnly
from users.models import Profile
from .permissions import CustomReadOnly

# Create your views here.


class QuestionView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [CustomReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
