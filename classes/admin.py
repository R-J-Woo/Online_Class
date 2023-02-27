from django.contrib import admin
from .models import Class

# Register your models here.


class ClassAdmin(admin.ModelAdmin):
    list_display = ('instructor', 'title',)


admin.site.register(Class, ClassAdmin)
