from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from Subject.apps import SubjectConfig

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class SubjectModel(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pass
# Create your views here.
