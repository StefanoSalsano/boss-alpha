#view for page three



from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import time
import datetime


def bugThree(request):
    request.session['sVar']['weight'] = "weight created from bug 3 m"
    #request.session.modfied = True
    ts = time.time()
    timeS3 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #sVar = request.session['sVar']
    #sVar ['weight'] = "weight created from bug 3 "
    #request.session['sVar'] = sVar
    return render ( request, 'myfirstapp/bug3.html', { 'bug3Out' : request.session['sVar'].values(),
                                                        'bug3Id' : request.session._session_key,
                                                        'bug3TS': timeS3 } )