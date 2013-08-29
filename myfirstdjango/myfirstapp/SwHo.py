#view to show Switches, Host

from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import json
import string    #module to manipolate the string

def switchesInfo(request):
    rSwOne = requests.get ( 'http://localhost:8080/wm/core/controller/switches/json' )    #it contains dpid address port 
    rSwTwo = requests.get ( 'http://localhost:8080/wm/core/switch/all/desc/json' )    #it contains manufacturer's' informations
    rHost = requests.get ( 'http://localhost:8080/wm/device/' )    #it contains host's' info
    request.session['switches'] = {}    #DEBUG dictionary that contains all informations about the switches. (local variable)
    host = {}    #dictionary that contains all informations about the hosts
    #if 'switches' not in request.session:
    for n in range ( len(rSwOne.json()) ):    #cycle to insert the switche's info in the dictionary "switches"
        temp = rSwOne.json()[n]['dpid']    #temp is a unicode type
        request.session['switches'][temp] = {}
        listemp = string.split ( rSwOne.json() [n] ['inetAddress'], ":" )    #to split address and port info
        request.session['switches'][temp]['SwAdd'] = listemp[0]
        request.session['switches'][temp]['SwContrPort'] = listemp[1]
        request.session ['switches'][temp] ['SwManuf'] = rSwTwo.json() [temp] [0] ['manufacturerDescription']
    
    #else:
        #for n in range ( len(rSwOne.json()) ):
            #temp = rSwOne.json() [n] ['dpid']
            #listemp = string.split ( rSwOne.json() [n] ['inetAddress'], ":" )
            #request.session ['switches'][temp] ['SwAdd'] = listemp[0]
            #request.session ['switches'][temp] ['SwContrPort'] = listemp[1]
            #request.session ['switches'][temp] ['SwManuf'] = rSwTwo.json() [temp] [0] ['manufacturerDescription']
    for n in range ( len (rHost.json()) ):    #cycle to insert HOST's info in the dictionary "host"
        temp = rHost.json() [n] ['mac'][0]
        host [temp] = {}
        if len ( rHost.json() [n] ['attachmentPoint'] ) > 0:    #it is necessary to have no errors when there aren't host connected
            host [temp] ['SwDpidAtt'] = rHost.json() [n] ['attachmentPoint'] [0] ['switchDPID']
            host [temp] ['SwPortAtt'] = rHost.json() [n] ['attachmentPoint'] [0] ['port']
            host [temp] ['ip'] = rHost.json() [n] ['ipv4'][0]
    #request.session.save()
    #request.session.modified = True
    return render (request, 'myfirstapp/SwHo.html', { 'SwDpid' : request.session['switches'].keys(),
                                                      'SwInfo' : request.session['switches'].values(),
                                                      'nSw' : len( request.session['switches'].keys() ),
                                                      'HMac' : host.keys(), 
                                                      'HInfo' : host.values(), 'nH' : len( host.keys() ), 
                                                      'bug' : request.session['switches'],
                                                      'bug1' : request.session._session_key,
                                                      'bug2' : len(rSwOne.json()) } )
