# view for debug

from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import json

def debug1(request):
    request.session['switches']['44:44:44:44:44:44:44:44']['SwManuf'] = "try change"
    #request.session.save()
    request.session.modified = True
    return render ( request, 'myfirstapp/debug1.html', { 'bugD' : request.session ['switches'],
                                                         'bug1D' : request.session._session_key}  )