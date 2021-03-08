from django.shortcuts import render
from django.views import generic
from .serializers import subjectSerializer
from .models import subject
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

class subjectModel(ListAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = subject.objects.all()
    serializer_class = subjectSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'subjectid': ['gte', 'lte', 'exact'],
        'height': ['gte', 'lte', 'exact'],
        'gender': ['gte', 'lte', 'exact'],
        'handedness': ['gte', 'lte', 'exact'],
        'birthyear': ['gte', 'lte', 'exact']
    }
    
    

    def get_queryset(self):
        #user = self.request.user
        return subject.objects.all()


    


# Create your views here.
