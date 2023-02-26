from django.db import models
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.


class Class(models.Model):
    instructor = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="강사", related_name="classes")
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, blank=True, verbose_name="강사 프로필")
    title = models.CharField(max_length=128, verbose_name="강의명")
    category = models.CharField(max_length=64, verbose_name="강의 카테고리")
    content = models.TextField(verbose_name="강의 내용")
    thumbnail = models.ImageField(verbose_name="강의 이미지")
    student = models.ManyToManyField(
        User, verbose_name="수강생", related_name="join_classes")
    recommend = models.ManyToManyField(
        User, verbose_name="추천", related_name="recommend_classes")
    register_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="수업 등록 날짜")
