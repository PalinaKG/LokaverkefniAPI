from msgolden.models import msgolden
from django.contrib import admin


@admin.register(msgolden)
class msgoldenAdmin(admin.ModelAdmin):
    list_display = ['msgoldenid', 'subjectid', 'type', 'dizziness', 'nausea', 'sweat', 'diffoffocus', 'blurredvision', 'incrsalvation', 'eyestrain','headache', 'fatigue','gendiscomfort']
