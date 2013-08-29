#view for page two


from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import time
import datetime



def bugTwo(request):
    request.session['sVar']['length'] = "length created from bug 2"
    #request.session.modfied = True
    ts = time.time()
    timeS2 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    #sVar = request.session['sVar']
    #sVar ['length'] = "length created from bug 2 "
    #request.session['sVar'] = sVar
    return render ( request, 'myfirstapp/bug2.html', { 'bug2Out' : request.session['sVar'].values(),
                                                        'bug2Id' : request.session._session_key,
                                                        'bug2TS': timeS2 } )
