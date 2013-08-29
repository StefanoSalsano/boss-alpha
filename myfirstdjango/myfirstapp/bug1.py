# view for page one

from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import time
import datetime


def bugOne(request):
    request.session['sVar'] = {}
    request.session['sVar']['index'] = "index one"
    #request.session['sVar']['length'] = "len one"
    #request.session['sVar']['weight'] = "weight one"
    #request.session.modfied = True
    ts = time.time()
    timeS1 = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return render ( request, 'myfirstapp/bug1.html', { 'bug1Out' : request.session['sVar'].values(),
                                                        'bug1Id' : request.session._session_key,
                                                        'bug1TS': timeS1 } )


