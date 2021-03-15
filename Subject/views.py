from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import generic
from .serializers import subjectSerializer
from .models import subject
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
import csv, io
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.views.decorators.csrf import csrf_exempt

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
    @csrf_exempt
    def add_sub(request):
        if request.method=='POST':
            sub=subject()

            data=request.body.decode('utf-8')
            data=data.split('\r\n')

            newData=[]
            for d in data:
                newData.append(d.split(","))
            subData=newData[1:]
            for d in subData:
                sub.subjectid=d[0]
                sub.height=d[1]
                sub.gender=d[2]
                sub.handedness=d[3]
                sub.birthyear=d[4]



            
            
        return HttpResponse()


    def get_queryset(self):
        #user = self.request.user
        return subject.objects.all()

# @csrf_exempt
# def subject_upload(request):
#     # template = "subject_upload.html"

#     # if request.method == "GET":
#     #     return render(request, template)
#     if request.method == "POST":
        
#         print("REQUEST: ")
#         print("HELLO",request)
#         print(request.FILES)

#         csv_file = request.FILES["file"]
#         print(csv_file)
#         if not csv_file.name.endwith('.csv'):
#             messages.error(request, 'This is not a csv file')

#         data_set = csv_file.read().decode('UTF-8')
#         io_string = io.stringIO(data_set)
#         next(io_string)
#         for column in csv.reader(io_string, delimiter = ',', quotechar="|"):
#             _, created = subject.objects.update_or_create(
#                 subjectid = column[0],
#                 height = column[1],
#                 gender = column[2],
#                 handedness = column[3],
#                 birthyear = column[4]
#             )

#         context = {}
#         return render(request, context)




# Create your views here.
