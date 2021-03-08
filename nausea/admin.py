from nausea.models import nausea
from django.contrib import admin


@admin.register(nausea)
class nauseaAdmin(admin.ModelAdmin):
    list_display = ['nauseaid', 'subjectid', 'trains', 'airplanes', 'smallboats', 'ships', 'swings', 'roundabout', 'funfair', 'busses','cars']