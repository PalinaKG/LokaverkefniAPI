from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from .models import hr
from subject.models import subject
from .serializers import hrSerializer
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponse


class hrModel(ListAPIView):

    queryset = hr.objects.all()
    serializer_class = hrSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['hrid', 'subjectid', 'bpm', 'interval']
    

    def get_queryset(self):
        #user = self.request.user
        return hr.objects.all()
