from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import emg
from .serializers import emgSerializer

class emgModel(ListAPIView):

    queryset = emg.objects.all()
    serializer_class = emgSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['emgid', 'subjectid', 'area', 'f40_132', 'f132_224', 'f224_316', 'f316_408', 'f408_500', 'interval', 'sensor']
    

    def get_queryset(self):
        #user = self.request.user
        return emg.objects.all()