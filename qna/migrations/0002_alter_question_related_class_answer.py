# Generated by Django 4.1.7 on 2023-03-01 09:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_profile_image"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("classes", "0003_alter_class_options"),
        ("qna", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="question",
            name="related_class",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="questions",
                to="classes.class",
                verbose_name="관련 수업",
            ),
        ),
        migrations.CreateModel(
            name="Answer",
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
                ("answer_text", models.TextField(verbose_name="답변 내용")),
                (
                    "register_dttm",
                    models.DateTimeField(auto_now_add=True, verbose_name="답변 등록 시간"),
                ),
                (
                    "answerer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="답변자",
                    ),
                ),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.profile",
                        verbose_name="답변자 프로필",
                    ),
                ),
                (
                    "question",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="answers",
                        to="qna.question",
                        verbose_name="관련 질문",
                    ),
                ),
            ],
        ),
    ]