from rest_framework import serializers
from .models import Question
from users.serializers import ProfileSerializer


class QuestionSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ("pk", "profile", "related_class",
                  "question_title", "question_text")


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("question_title", "question_text")
