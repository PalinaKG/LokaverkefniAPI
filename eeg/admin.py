from eeg.models import eeg
from django.contrib import admin


@admin.register(eeg)
class eegAdmin(admin.ModelAdmin):
    list_display = ['eegid', 'subjectid', 'alpha', 'beta', 'theta', 'low_gamma', 'delta', 'interval']