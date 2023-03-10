# Generated by Django 4.1.7 on 2023-02-26 07:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("users", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Class",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=128, verbose_name="강의명")),
                ("category", models.CharField(max_length=64, verbose_name="강의 카테고리")),
                ("content", models.TextField(verbose_name="강의 내용")),
                ("thumbnail", models.ImageField(upload_to="", verbose_name="강의 이미지")),
                (
                    "register_dttm",
                    models.DateTimeField(auto_now_add=True, verbose_name="수업 등록 날짜"),
                ),
                (
                    "instructor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="강사",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.profile",
                        verbose_name="강사 프로필",
                    ),
                ),
                (
                    "recommend",
                    models.ManyToManyField(
                        related_name="recommend_classes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="추천",
                    ),
                ),
                (
                    "student",
                    models.ManyToManyField(
                        related_name="join_classes",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="수강생",
                    ),
                ),
            ],
        ),
    ]
