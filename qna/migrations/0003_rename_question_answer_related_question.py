# Generated by Django 4.1.7 on 2023-03-02 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("qna", "0002_alter_question_related_class_answer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="answer", old_name="question", new_name="related_question",
        ),
    ]
