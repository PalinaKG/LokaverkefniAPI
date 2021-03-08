from emg.models import emg
from django.contrib import admin


@admin.register(emg)
class emgAdmin(admin.ModelAdmin):
    list_display = ['emgid', 'subjectid', 'area', 'f40_132', 'f132_224', 'f224_316', 'f316_408', 'f408_500', 'interval', 'sensor']