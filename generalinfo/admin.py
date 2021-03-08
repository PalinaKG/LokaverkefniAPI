from generalinfo.models import generalinfo
from django.contrib import admin


@admin.register(generalinfo)
class generalinfoAdmin(admin.ModelAdmin):
    list_display = ['genid', 'subjectid', 'foodtime', 'caffeine', 'weight', 'healthyscale', 'groups', 'nicotine', 'noexercise', 'alcohol','msdrugs','motionsickness','comments']