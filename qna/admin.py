from django.contrib import admin
from .models import Question

# Register your models here.


class QuesetionAdmin(admin.ModelAdmin):
    list_display = ('related_class', 'questioner', 'question_title',)


admin.site.register(Question, QuesetionAdmin)

# Register your models here.
