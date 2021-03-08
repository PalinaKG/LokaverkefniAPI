from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import spo2
from .serializers import spo2Serializer

class spo2Model(ListAPIView):
    queryset = spo2.objects.all()
    serializer_class = spo2Serializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['spo2id', 'subjectid', 'oxigenation', 'time']


    def get_queryset(self):
        #user = self.request.user
        return spo2.objects.all()
    