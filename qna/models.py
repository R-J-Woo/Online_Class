from django.db import models
from classes.models import Class
from users.models import Profile
from django.contrib.auth.models import User
# Create your models here.


class Question(models.Model):
    questioner = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="질문자")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="질문자 프로필")
    related_class = models.ForeignKey(
        Class, related_name="questions", on_delete=models.CASCADE, verbose_name="관련 수업")
    question_title = models.CharField(max_length=128, verbose_name="질문 제목")
    question_text = models.TextField(verbose_name="질문 내용")
    register_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="질문 등록 시간")


class Answer(models.Model):
    answerer = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="답변자")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="답변자 프로필")
    related_question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE, verbose_name="관련 질문")
    answer_text = models.TextField(verbose_name="답변 내용")
    register_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="답변 등록 시간")
