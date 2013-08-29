#view for page four



from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import time
import datetime


def bugFour(request):
    request.session['sVar']['try'] = "try changed from bug 4"
    #request.session.modfied = True
    ts = time.time()
    timeS4 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return render ( request, 'myfirstapp/bug4.html', { 'bug4Out' : request.session['sVar'].values(),
                                                        'bug4Id' : request.session._session_key,
                                                        'bug4TS': timeS4 } )