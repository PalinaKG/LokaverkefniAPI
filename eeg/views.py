from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import eeg
from .serializers import eegSerializer

class eegModel(ListAPIView):

    queryset = eeg.objects.all()
    serializer_class = eegSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['eegid', 'subjectid', 'alpha', 'beta', 'theta', 'low_gamma', 'delta', 'interval', 'sensor']

    def get_queryset(self):
        #user = self.request.user
        return eeg.objects.all()