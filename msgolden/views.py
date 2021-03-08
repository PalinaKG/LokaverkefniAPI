from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import msgolden
from .serializers import msgoldenSerializer

class msgoldenModel(ListAPIView):

    queryset = msgolden.objects.all()
    serializer_class = msgoldenSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['msgoldenid', 'subjectid', 'type', 'dizziness', 'nausea', 'sweat', 'diffoffocus', 'blurredvision', 'incrsalvation', 'eyestrain','headache', 'fatigue','gendiscomfort']
    

    def get_queryset(self):
        #user = self.request.user
        return msgolden.objects.all()