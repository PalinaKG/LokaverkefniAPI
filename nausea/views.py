from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import nausea
from .serializers import nauseaSerializer

class nauseaModel(ListAPIView):
    queryset = nausea.objects.all()
    serializer_class = nauseaSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nauseaid', 'subjectid', 'trains', 'airplanes', 'smallboats', 'ships', 'swings', 'roundabout', 'funfair', 'busses','cars']
    

    def get_queryset(self):
        #user = self.request.user
        return nausea.objects.all()