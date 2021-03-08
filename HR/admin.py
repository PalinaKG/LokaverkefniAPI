from hr.models import hr
from django.contrib import admin


@admin.register(hr)
class hrAdmin(admin.ModelAdmin):
    list_display = ['hrid', 'subjectid', 'bpm', 'time']