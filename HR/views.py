from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import hr
from .serializers import hrSerializer

class hrModel(ListAPIView):

    queryset = hr.objects.all()
    serializer_class = hrSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hrid', 'subjectid', 'bpm', 'time']
    

    def get_queryset(self):
        #user = self.request.user
        return hr.objects.all()