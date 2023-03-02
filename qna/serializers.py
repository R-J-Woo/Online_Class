from rest_framework import serializers
from .models import Question, Answer
from users.serializers import ProfileSerializer


class AnswerSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ("pk", "profile", "related_question", "answer_text")


class AnswerCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ("related_question", "answer_text")


class QuestionSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only=True)
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ("pk", "profile", "related_class",
                  "question_title", "question_text", "answers")


class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("question_title", "question_text")
