from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import generalinfo
from .serializers import generalinfoSerializer

class generalinfoModel(ListAPIView):

    queryset = generalinfo.objects.all()
    serializer_class = generalinfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genid', 'subjectid', 'foodtime', 'caffeine', 'weight', 'healthyscale', 'groups', 'nicotine', 'noexercise', 'alcohol','msdrugs','motionsickness','comments']
    


    def get_queryset(self):
        #user = self.request.user
        return generalinfo.objects.all()