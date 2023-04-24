from django.contrib import admin
from .models import Question, Answer

# Register your models here.


class QuesetionAdmin(admin.ModelAdmin):
    list_display = ('related_class', 'questioner', 'question_title',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('related_question', 'answerer',)


admin.site.register(Question, QuesetionAdmin)
admin.site.register(Answer, AnswerAdmin)

# Register your models here.
