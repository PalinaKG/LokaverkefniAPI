from spo2.models import spo2
from django.contrib import admin


@admin.register(spo2)
class spo2Admin(admin.ModelAdmin):
    list_display = ['spo2id', 'subjectid', 'oxigenation', 'time']