from django.db import models
from django.http import response
from rest_framework.response import Response

from hr.models import hr as hrModel
from eeg.models import eeg as eegModel
from emg.models import emg as emgModel
from subject.models import subject
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework import status
from rest_framework.decorators import api_view



class MyCustomExcpetion(PermissionDenied):
    # status_code = status.HTTP_400_BAD_REQUEST
    # default_detail = "Custom Exception Message"
    # default_code = 'invalid'

    def __init__(self, detail, status_code=None):
        self.detail = detail
        if status_code is not None:
            self.status_code = status_code

@api_view(['POST'])
@csrf_exempt
def import_data(request):
    if request.method=='POST':
        data=request.body.decode('utf-8')
        data=data.split('\r\n')
        newData=[]
        for d in data:
            parsedData=parseData(d)
            newData.append(parsedData.split(','))
        [headersOK, whichHeader]=checkHeaders(newData[0])
        print(headersOK)
        print(whichHeader)
        if headersOK==False:
            response = {'data': whichHeader}
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        else:
            data=newData[1:] #Removing the header
            for d in data:
                sub=get_object_or_404(subject, pk=d[0])
                for i in range(0, 5):
                    hr = hrModel()
                    hr.subjectid = sub
                    hr.bpm = d[2+i]
                    hr.interval = i
                    # hr.save()
                counter = 0
                for i in range(0, 30, 5): 
                    eeg = eegModel()
                    eeg.subjectid = sub
                    eeg.delta = d[7+i]
                    eeg.theta = d[8+i]
                    eeg.alpha = d[9+i]
                    eeg.beta = d[10+i]
                    eeg.low_gamma = d[11+i]
                    eeg.interval = counter
                    counter = counter+1
                    # eeg.save()
                counter=0
                for k in range(0,5):
                    for i in range(0, 35, 5): 
                        emg = emgModel()
                        emg.subjectid = sub
                        emg.area = d[37+counter+k*6]
                        emg.f40_132 = d[73+i+k*30]
                        emg.f132_224 = d[74+i+k*30]
                        emg.f224_316 = d[75+i+k*30]
                        emg.f316_408 = d[76+i+k*30]
                        emg.f408_500 = d[77+i+k*30]
                        emg.sensor = counter+1
                        emg.interval = k
                        counter=counter+1
                        # emg.save()
                    counter=0     
    return response.HttpResponse


def parseData(data):
    newData=''
    startString = False
    for i in range(0,len(data)):  
        if data[i] == '"' and startString==False:
            startString = True
        elif data[i] == '"' and startString==True:
            startString = False
        elif startString == True:
            if data[i] == ',':
                newData+=''
            else:
                newData+=data[i]
        else:
            newData+=data[i]
    return newData


def checkHeaders(data):
    print(data[0])
    counter=0
    
    if data[counter] != 'Suject ID':
        return [False, 'Subject ID']
    counter=counter+1
    if data[counter] != 'Concussion':
        return [False, 'Concussion']
    counter=counter+1
    if data[counter] != 'HR PRE':
        return [False, 'HR PRE']
    counter=counter+1
    if data[counter] != 'HR 25':
        return [False, 'HR 25']
    counter=counter+1
    if data[counter] != 'HR 50':
        return [False, 'HR 50']
    counter=counter+1
    if data[counter] != 'HR 75':
        return [False, 'HR 75']
    counter=counter+1
    if data[counter] != 'HR POST':
        return [False, 'HR POST']
    counter=counter+1


    if data[counter] != 'EEG DELTA BL':
        return [False, 'EEG DELTA BL']
    counter=counter+1
    if data[counter] != 'EEG THETA BL':
        return [False, 'EEG THETA BL']
    counter=counter+1
    if data[counter] != 'EEG ALPHA BL':
        return [False, 'EEG ALPHA BL']
    counter=counter+1
    if data[counter] != 'EEG BETA BL':
        return [False, 'EEG BETA BL']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA BL':
        return [False, 'EEG LOWGAMMA BL']
    counter=counter+1

    if data[counter] != 'EEG DELTA PRE':
        return [False, 'EEG DELTA PRE']
    counter=counter+1
    if data[counter] != 'EEG THETA PRE':
        return [False, 'EEG THETA PRE']
    counter=counter+1
    if data[counter] != 'EEG ALPHA PRE':
        return [False, 'EEG ALPHA PRE']
    counter=counter+1
    if data[counter] != 'EEG BETA PRE':
        return [False, 'EEG BETA PRE']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA PRE':
        return [False, 'EEG LOWGAMMA PRE']
    counter=counter+1


    if data[counter] != 'EEG DELTA 25':
        return [False, 'EEG DELTA 25']
    counter=counter+1
    if data[counter] != 'EEG THETA 25':
        return [False, 'EEG THETA 25']
    counter=counter+1
    if data[counter] != 'EEG ALPHA 25':
        return [False, 'EEG ALPHA 25']
    counter=counter+1
    if data[counter] != 'EEG BETA 25':
        return [False, 'EEG BETA 25']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA 25':
        return [False, 'EEG LOWGAMMA 25']
    counter=counter+1


    if data[counter] != 'EEG DELTA 50':
        return [False, 'EEG DELTA 50']
    counter=counter+1
    if data[counter] != 'EEG THETA 50':
        return [False, 'EEG THETA 50']
    counter=counter+1
    if data[counter] != 'EEG ALPHA 50':
        return [False, 'EEG ALPHA 50']
    counter=counter+1
    if data[counter] != 'EEG BETA 50':
        return [False, 'EEG BETA 50']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA 50':
        return [False, 'EEG LOWGAMMA 50']
    counter=counter+1


    if data[counter] != 'EEG DELTA 75':
        return [False, 'EEG DELTA 75']
    counter=counter+1
    if data[counter] != 'EEG THETA 75':
        return [False, 'EEG THETA 75']
    counter=counter+1
    if data[counter] != 'EEG ALPHA 75':
        return [False, 'EEG ALPHA 75']
    counter=counter+1
    if data[counter] != 'EEG BETA 75':
        return [False, 'EEG BETA 75']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA 75':
        return [False, 'EEG LOWGAMMA 75']
    counter=counter+1

    if data[counter] != 'EEG DELTA POST':
        return [False, 'EEG DELTA POST']
    counter=counter+1
    if data[counter] != 'EEG THETA POST':
        return [False, 'EEG THETA POST']
    counter=counter+1
    if data[counter] != 'EEG ALPHA POST':
        return [False, 'EEG ALPHA POST']
    counter=counter+1
    if data[counter] != 'EEG BETA POST':
        return [False, 'EEG BETA POST']
    counter=counter+1
    if data[counter] != 'EEG LOWGAMMA POST':
        return [False, 'EEG LOWGAMMA POST']
    counter=counter+1


    if data[counter] != 'AREA EMG 1 BSL':
        return [False, 'AREA EMG 1 BSL']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 BSL':
        return [False, 'AREA EMG 2 BSL']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 BSL':
        return [False, 'AREA EMG 3 BSL']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 BSL':
        return [False, 'AREA EMG 4 BSL']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 BSL':
        return [False, 'AREA EMG 5 BSL']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 BSL':
        return [False, 'AREA EMG 6 BSL']
    counter=counter+1

    if data[counter] != 'AREA EMG 1 PRE':
        return [False, 'AREA EMG 1 PRE']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 PRE':
        return [False, 'AREA EMG 2 PRE']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 PRE':
        return [False, 'AREA EMG 3 PRE']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 PRE':
        return [False, 'AREA EMG 4 PRE']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 PRE':
        return [False, 'AREA EMG 5 PRE']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 PRE':
        return [False, 'AREA EMG 6 PRE']
    counter=counter+1

    if data[counter] != 'AREA EMG 1 25':
        return [False, 'AREA EMG 1 25']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 25':
        return [False, 'AREA EMG 2 25']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 25':
        return [False, 'AREA EMG 3 25']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 25':
        return [False, 'AREA EMG 4 25']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 25':
        return [False, 'AREA EMG 5 25']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 25':
        return [False, 'AREA EMG 6 25']
    counter=counter+1

    if data[counter] != 'AREA EMG 1 50':
        return [False, 'AREA EMG 1 50']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 50':
        return [False, 'AREA EMG 2 50']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 50':
        return [False, 'AREA EMG 3 50']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 50':
        return [False, 'AREA EMG 4 50']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 50':
        return [False, 'AREA EMG 5 50']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 50':
        return [False, 'AREA EMG 6 50']
    counter=counter+1

    if data[counter] != 'AREA EMG 1 75':
        return [False, 'AREA EMG 1 75']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 75':
        return [False, 'AREA EMG 2 75']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 75':
        return [False, 'AREA EMG 3 75']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 75':
        return [False, 'AREA EMG 4 75']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 75':
        return [False, 'AREA EMG 5 75']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 75':
        return [False, 'AREA EMG 6 75']
    counter=counter+1

    if data[counter] != 'AREA EMG 1 Post':
        return [False, 'AREA EMG 1 Post']
    counter=counter+1
    if data[counter] != 'AREA EMG 2 Post':
        return [False, 'AREA EMG 2 Post']
    counter=counter+1
    if data[counter] != 'AREA EMG 3 Post':
        return [False, 'AREA EMG 3 Post']
    counter=counter+1
    if data[counter] != 'AREA EMG 4 Post':
        return [False, 'AREA EMG 4 Post']
    counter=counter+1
    if data[counter] != 'AREA EMG 5 Post':
        return [False, 'AREA EMG 5 Post']
    counter=counter+1
    if data[counter] != 'AREA EMG 6 Post':
        return [False, 'AREA EMG 6 Post']
    counter=counter+1

    if data[counter] != '1 40-132 Hz BSL':
        return [False, '1 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '1 133-224 Hz BSL':
        return [False, '1 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '1 225-316 Hz BSL':
        return [False, '1 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '1 317-408 Hz BSL':
        return [False, '1 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '1 409-500 Hz BSL':
        return [False, '1 409-500 Hz BSL']
    counter=counter+1


    if data[counter] != '2 40-132 Hz BSL':
        return [False, '2 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '2 133-224 Hz BSL':
        return [False, '2 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '2 225-316 Hz BSL':
        return [False, '2 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '2 317-408 Hz BSL':
        return [False, '2 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '2 409-500 Hz BSL':
        return [False, '2 409-500 Hz BSL']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz BSL':
        return [False, '3 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '3 133-224 Hz BSL':
        return [False, '3 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '3 225-316 Hz BSL':
        return [False, '3 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '3 317-408 Hz BSL':
        return [False, '3 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '3 409-500 Hz BSL':
        return [False, '3 409-500 Hz BSL']
    counter=counter+1

    if data[counter] != '4 40-132 Hz BSL':
        return [False, '4 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '4 133-224 Hz BSL':
        return [False, '4 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '4 225-316 Hz BSL':
        return [False, '4 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '4 317-408 Hz BSL':
        return [False, '4 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '4 409-500 Hz BSL':
        return [False, '4 409-500 Hz BSL']
    counter=counter+1
    if data[counter] != '5 40-132 Hz BSL':
        return [False, '5 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '5 133-224 Hz BSL':
        return [False, '5 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '5 225-316 Hz BSL':
        return [False, '5 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '5 317-408 Hz BSL':
        return [False, '5 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '5 409-500 Hz BSL':
        return [False, '5 409-500 Hz BSL']
    counter=counter+1

    if data[counter] != '6 40-132 Hz BSL':
        return [False, '6 40-132 Hz BSL']
    counter=counter+1
    if data[counter] != '6 133-224 Hz BSL':
        return [False, '6 133-224 Hz BSL']
    counter=counter+1
    if data[counter] != '6 225-316 Hz BSL':
        return [False, '6 225-316 Hz BSL']
    counter=counter+1
    if data[counter] != '6 317-408 Hz BSL':
        return [False, '6 317-408 Hz BSL']
    counter=counter+1
    if data[counter] != '6 409-500 Hz BSL':
        return [False, '6 409-500 Hz BSL']
    counter=counter+1

    if data[counter] != '1 40-132 Hz Pre':
        return [False, '1 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '1 133-224 Hz Pre':
        return [False, '1 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '1 225-316 Hz Pre':
        return [False, '1 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '1 317-408 Hz Pre':
        return [False, '1 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '1 409-500 Hz Pre':
        return [False, '1 409-500 Hz Pre']
    counter=counter+1


    if data[counter] != '2 40-132 Hz Pre':
        return [False, '2 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '2 133-224 Hz Pre':
        return [False, '2 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '2 225-316 Hz Pre':
        return [False, '2 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '2 317-408 Hz Pre':
        return [False, '2 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '2 409-500 Hz Pre':
        return [False, '2 409-500 Hz Pre']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz Pre':
        return [False, '3 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '3 133-224 Hz Pre':
        return [False, '3 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '3 225-316 Hz Pre':
        return [False, '3 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '3 317-408 Hz Pre':
        return [False, '3 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '3 409-500 Hz Pre':
        return [False, '3 409-500 Hz Pre']
    counter=counter+1

    if data[counter] != '4 40-132 Hz Pre':
        return [False, '4 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '4 133-224 Hz Pre':
        return [False, '4 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '4 225-316 Hz Pre':
        return [False, '4 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '4 317-408 Hz Pre':
        return [False, '4 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '4 409-500 Hz Pre':
        return [False, '4 409-500 Hz Pre']
    counter=counter+1
    
    if data[counter] != '5 40-132 Hz Pre':
        return [False, '5 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '5 133-224 Hz Pre':
        return [False, '5 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '5 225-316 Hz Pre':
        return [False, '5 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '5 317-408 Hz Pre':
        return [False, '5 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '5 409-500 Hz Pre':
        return [False, '5 409-500 Hz Pre']
    counter=counter+1

    if data[counter] != '6 40-132 Hz Pre':
        return [False, '6 40-132 Hz Pre']
    counter=counter+1
    if data[counter] != '6 133-224 Hz Pre':
        return [False, '6 133-224 Hz Pre']
    counter=counter+1
    if data[counter] != '6 225-316 Hz Pre':
        return [False, '6 225-316 Hz Pre']
    counter=counter+1
    if data[counter] != '6 317-408 Hz Pre':
        return [False, '6 317-408 Hz Pre']
    counter=counter+1
    if data[counter] != '6 409-500 Hz Pre':
        return [False, '6 409-500 Hz Pre']
    counter=counter+1

    if data[counter] != '1 40-132 Hz 25':
        return [False, '1 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '1 133-224 Hz 25':
        return [False, '1 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '1 225-316 Hz 25':
        return [False, '1 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '1 317-408 Hz 25':
        return [False, '1 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '1 409-500 Hz 25':
        return [False, '1 409-500 Hz 25']
    counter=counter+1


    if data[counter] != '2 40-132 Hz 25':
        return [False, '2 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '2 133-224 Hz 25':
        return [False, '2 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '2 225-316 Hz 25':
        return [False, '2 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '2 317-408 Hz 25':
        return [False, '2 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '2 409-500 Hz 25':
        return [False, '2 409-500 Hz 25']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz 25':
        return [False, '3 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '3 133-224 Hz 25':
        return [False, '3 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '3 225-316 Hz 25':
        return [False, '3 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '3 317-408 Hz 25':
        return [False, '3 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '3 409-500 Hz 25':
        return [False, '3 409-500 Hz 25']
    counter=counter+1

    if data[counter] != '4 40-132 Hz 25':
        return [False, '4 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '4 133-224 Hz 25':
        return [False, '4 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '4 225-316 Hz 25':
        return [False, '4 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '4 317-408 Hz 25':
        return [False, '4 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '4 409-500 Hz 25':
        return [False, '4 409-500 Hz 25']
    counter=counter+1
    
    if data[counter] != '5 40-132 Hz 25':
        return [False, '5 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '5 133-224 Hz 25':
        return [False, '5 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '5 225-316 Hz 25':
        return [False, '5 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '5 317-408 Hz 25':
        return [False, '5 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '5 409-500 Hz 25':
        return [False, '5 409-500 Hz 25']
    counter=counter+1

    if data[counter] != '6 40-132 Hz 25':
        return [False, '6 40-132 Hz 25']
    counter=counter+1
    if data[counter] != '6 133-224 Hz 25':
        return [False, '6 133-224 Hz 25']
    counter=counter+1
    if data[counter] != '6 225-316 Hz 25':
        return [False, '6 225-316 Hz 25']
    counter=counter+1
    if data[counter] != '6 317-408 Hz 25':
        return [False, '6 317-408 Hz 25']
    counter=counter+1
    if data[counter] != '6 409-500 Hz 25':
        return [False, '6 409-500 Hz 25']
    counter=counter+1

    if data[counter] != '1 40-132 Hz 50':
        return [False, '1 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '1 133-224 Hz 50':
        return [False, '1 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '1 225-316 Hz 50':
        return [False, '1 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '1 317-408 Hz 50':
        return [False, '1 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '1 409-500 Hz 50':
        return [False, '1 409-500 Hz 50']
    counter=counter+1


    if data[counter] != '2 40-132 Hz 50':
        return [False, '2 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '2 133-224 Hz 50':
        return [False, '2 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '2 225-316 Hz 50':
        return [False, '2 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '2 317-408 Hz 50':
        return [False, '2 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '2 409-500 Hz 50':
        return [False, '2 409-500 Hz 50']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz 50':
        return [False, '3 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '3 133-224 Hz 50':
        return [False, '3 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '3 225-316 Hz 50':
        return [False, '3 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '3 317-408 Hz 50':
        return [False, '3 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '3 409-500 Hz 50':
        return [False, '3 409-500 Hz 50']
    counter=counter+1

    if data[counter] != '4 40-132 Hz 50':
        return [False, '4 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '4 133-224 Hz 50':
        return [False, '4 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '4 225-316 Hz 50':
        return [False, '4 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '4 317-408 Hz 50':
        return [False, '4 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '4 409-500 Hz 50':
        return [False, '4 409-500 Hz 50']
    counter=counter+1
    
    if data[counter] != '5 40-132 Hz 50':
        return [False, '5 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '5 133-224 Hz 50':
        return [False, '5 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '5 225-316 Hz 50':
        return [False, '5 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '5 317-408 Hz 50':
        return [False, '5 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '5 409-500 Hz 50':
        return [False, '5 409-500 Hz 50']
    counter=counter+1

    if data[counter] != '6 40-132 Hz 50':
        return [False, '6 40-132 Hz 50']
    counter=counter+1
    if data[counter] != '6 133-224 Hz 50':
        return [False, '6 133-224 Hz 50']
    counter=counter+1
    if data[counter] != '6 225-316 Hz 50':
        return [False, '6 225-316 Hz 50']
    counter=counter+1
    if data[counter] != '6 317-408 Hz 50':
        return [False, '6 317-408 Hz 50']
    counter=counter+1
    if data[counter] != '6 409-500 Hz 50':
        return [False, '6 409-500 Hz 50']
    counter=counter+1

    if data[counter] != '1 40-132 Hz 75':
        return [False, '1 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '1 133-224 Hz 75':
        return [False, '1 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '1 225-316 Hz 75':
        return [False, '1 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '1 317-408 Hz 75':
        return [False, '1 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '1 409-500 Hz 75':
        return [False, '1 409-500 Hz 75']
    counter=counter+1


    if data[counter] != '2 40-132 Hz 75':
        return [False, '2 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '2 133-224 Hz 75':
        return [False, '2 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '2 225-316 Hz 75':
        return [False, '2 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '2 317-408 Hz 75':
        return [False, '2 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '2 409-500 Hz 75':
        return [False, '2 409-500 Hz 75']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz 75':
        return [False, '3 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '3 133-224 Hz 75':
        return [False, '3 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '3 225-316 Hz 75':
        return [False, '3 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '3 317-408 Hz 75':
        return [False, '3 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '3 409-500 Hz 75':
        return [False, '3 409-500 Hz 75']
    counter=counter+1

    if data[counter] != '4 40-132 Hz 75':
        return [False, '4 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '4 133-224 Hz 75':
        return [False, '4 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '4 225-316 Hz 75':
        return [False, '4 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '4 317-408 Hz 75':
        return [False, '4 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '4 409-500 Hz 75':
        return [False, '4 409-500 Hz 75']
    counter=counter+1
    
    if data[counter] != '5 40-132 Hz 75':
        return [False, '5 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '5 133-224 Hz 75':
        return [False, '5 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '5 225-316 Hz 75':
        return [False, '5 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '5 317-408 Hz 75':
        return [False, '5 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '5 409-500 Hz 75':
        return [False, '5 409-500 Hz 75']
    counter=counter+1

    if data[counter] != '6 40-132 Hz 75':
        return [False, '6 40-132 Hz 75']
    counter=counter+1
    if data[counter] != '6 133-224 Hz 75':
        return [False, '6 133-224 Hz 75']
    counter=counter+1
    if data[counter] != '6 225-316 Hz 75':
        return [False, '6 225-316 Hz 75']
    counter=counter+1
    if data[counter] != '6 317-408 Hz 75':
        return [False, '6 317-408 Hz 75']
    counter=counter+1
    if data[counter] != '6 409-500 Hz 75':
        return [False, '6 409-500 Hz 75']
    counter=counter+1


    if data[counter] != '1 40-132 Hz Post':
        return [False, '1 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '1 133-224 Hz Post':
        return [False, '1 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '1 225-316 Hz Post':
        return [False, '1 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '1 317-408 Hz Post':
        return [False, '1 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '1 409-500 Hz Post':
        return [False, '1 409-500 Hz Post']
    counter=counter+1


    if data[counter] != '2 40-132 Hz Post':
        return [False, '2 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '2 133-224 Hz Post':
        return [False, '2 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '2 225-316 Hz Post':
        return [False, '2 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '2 317-408 Hz Post':
        return [False, '2 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '2 409-500 Hz Post':
        return [False, '2 409-500 Hz Post']
    counter=counter+1
    

    if data[counter] != '3 40-132 Hz Post':
        return [False, '3 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '3 133-224 Hz Post':
        return [False, '3 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '3 225-316 Hz Post':
        return [False, '3 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '3 317-408 Hz Post':
        return [False, '3 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '3 409-500 Hz Post':
        return [False, '3 409-500 Hz Post']
    counter=counter+1

    if data[counter] != '4 40-132 Hz Post':
        return [False, '4 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '4 133-224 Hz Post':
        return [False, '4 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '4 225-316 Hz Post':
        return [False, '4 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '4 317-408 Hz Post':
        return [False, '4 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '4 409-500 Hz Post':
        return [False, '4 409-500 Hz Post']
    counter=counter+1
    
    if data[counter] != '5 40-132 Hz Post':
        return [False, '5 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '5 133-224 Hz Post':
        return [False, '5 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '5 225-316 Hz Post':
        return [False, '5 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '5 317-408 Hz Post':
        return [False, '5 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '5 409-500 Hz Post':
        return [False, '5 409-500 Hz Post']
    counter=counter+1

    if data[counter] != '6 40-132 Hz Post':
        return [False, '6 40-132 Hz Post']
    counter=counter+1
    if data[counter] != '6 133-224 Hz Post':
        return [False, '6 133-224 Hz Post']
    counter=counter+1
    if data[counter] != '6 225-316 Hz Post':
        return [False, '6 225-316 Hz Post']
    counter=counter+1
    if data[counter] != '6 317-408 Hz Post':
        return [False, '6 317-408 Hz Post']
    counter=counter+1
    if data[counter] != '6 409-500 Hz Post':
        return [False, '6 409-500 Hz Post']
    counter=counter+1

    


    return [True, '']
