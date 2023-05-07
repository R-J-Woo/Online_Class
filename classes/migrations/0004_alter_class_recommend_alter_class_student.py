# Generated by Django 4.1.7 on 2023-05-05 07:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("classes", "0003_alter_class_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="recommend",
            field=models.ManyToManyField(
                blank=True,
                related_name="recommend_classes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="추천",
            ),
        ),
        migrations.AlterField(
            model_name="class",
            name="student",
            field=models.ManyToManyField(
                blank=True,
                related_name="join_classes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="수강생",
            ),
        ),
    ]