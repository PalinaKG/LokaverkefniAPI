from subject.models import subject
from django.contrib import admin


@admin.register(subject)
class subjectAdmin(admin.ModelAdmin):
    list_display = ['subjectid','height', 'gender', 'handedness', 'birthyear']