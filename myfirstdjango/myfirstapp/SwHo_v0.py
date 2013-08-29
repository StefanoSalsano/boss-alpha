#view to show Switches, Host

from django.shortcuts import render
import requests
import json
import string    #module to manipolate the string

def switchesInfo(request):
    rSwOne = requests.get ( 'http://localhost:8080/wm/core/controller/switches/json' )    #it contains dpid address port 
    rSwTwo = requests.get ( 'http://localhost:8080/wm/core/switch/all/desc/json' )    #it contains manufacturer's' informations
    rHost = requests.get ( 'http://localhost:8080/wm/device/' )    #it contains host's' info
    switches = {}    #dictionary that contains all informations about the switches
    host = {}    #dictionary that contains all informations about the hosts
    for n in range ( len(rSwOne.json()) ):    #cycle to insert the switche's info in the dictionary "switches"
        temp = rSwOne.json() [n] ['dpid']    #temp is a unicode type
        switches [temp] = {}
        listemp = string.split ( rSwOne.json() [n] ['inetAddress'], ":" )    #to split address and port info
        switches [temp] ['SwAdd'] = listemp[0]
        switches [temp] ['SwContPort'] = listemp[1]
        switches [temp] ['SwManuf'] = rSwTwo.json() [temp] [0] ['manufacturerDescription']
    for n in range ( len (rHost.json()) ):    #cycle to insert HOST's info in the dictionary "host"
        temp = rHost.json() [n] ['mac'][0]
        host [temp] = {}
        host [temp] ['ip'] = rHost.json() [n] ['ipv4'][0]
        host [temp] ['SwDpidAtt'] = rHost.json() [n] ['attachmentPoint'] [0] ['switchDPID']
        host [temp] ['SwPortAtt'] = rHost.json() [n] ['attachmentPoint'] [0] ['port']
    return render (request, 'myfirstapp/switches.html', { 'SwDpid' : switches.keys(), 'SwInfo' : switches.values(),
                                                        'nSw' : len( switches.keys() ), 'HMac' : host.keys(), 
                                                        'HInfo' : host.values(), 'nH' : len( host.keys() ), } )
