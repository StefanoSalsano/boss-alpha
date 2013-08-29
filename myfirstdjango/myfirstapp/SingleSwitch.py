#view for single switch and flows informations

from django.contrib.sessions.models import Session
from django.shortcuts import render
import requests
import json

def singleSwitch(request, DpidUrl):    #DpidUrl is needed for dinamic url request
    rSinSwOne = requests.get ( 'http://localhost:8080/wm/core/switch/'+DpidUrl+'/features/json' )    #I RestApi Switch
    rSinSwTwo = requests.get ( 'http://localhost:8080/wm/core/switch/'+DpidUrl+'/port/json' )    #II RestApi Switch
    rSFlow = requests.get ('http://localhost:8080/wm/core/switch/'+DpidUrl+'/flow/json')    #RestApi Flow
    singleSw = {}    #dictionary that contains info about single switch. The key is the switch dpid
    singleSw [DpidUrl] = {}
    flow = {}    #dictionary with the info of the flows
    flow[DpidUrl] = []    #LIST Each element is one flow
    request.session['switches'][DpidUrl]['flows'] = {}    #DEBUG to try session variable
    request.session['switches'][DpidUrl]['flows'] ['firstflow'] = "flowOne"    #DEBUG
    #switches = request.session['switches']
    #switches[DpidUrl]['flows'] = {}
    #switches[DpidUrl]['flows']['firstflow'] = "flowOne"
    for n in range( len(rSinSwOne.json()[DpidUrl]['ports']) ):    #it takes info from first restapi (about ports Switches)
        temp = rSinSwOne.json()[DpidUrl]['ports'][n]['portNumber']    #it needed to use the port number as a key
        singleSw [DpidUrl] [temp] = {}    #it creates the port number as a key
        singleSw [DpidUrl] [temp]['pName'] = rSinSwOne.json()[DpidUrl]['ports'][n]['name']
        tempT = rSinSwOne.json()[DpidUrl]['ports'][n]['state']
        if tempT == 0:    #to change state info 0 with up and 1 with down 
            singleSw [DpidUrl][temp]['pState'] = 'UP'
        else:
            singleSw [DpidUrl][temp]['pState'] = 'DOWN'
        singleSw [DpidUrl] [temp]['pMac'] = rSinSwOne.json()[DpidUrl]['ports'][n]['hardwareAddress']
    for n in range( len(rSinSwTwo.json()[DpidUrl]) ):    #it takes info from second restapi (about port Switches)
        temp = rSinSwTwo.json()[DpidUrl][n]['portNumber']
        singleSw [DpidUrl][temp]['pTxB'] = rSinSwTwo.json()[DpidUrl][n]['transmitBytes']
        singleSw [DpidUrl][temp]['pRxB'] = rSinSwTwo.json()[DpidUrl][n]['receiveBytes']
        singleSw [DpidUrl][temp]['pTxP'] = rSinSwTwo.json()[DpidUrl][n]['transmitPackets']
        singleSw [DpidUrl][temp]['pRxP'] = rSinSwTwo.json()[DpidUrl][n]['receivePackets']
        singleSw [DpidUrl][temp]['pTxDrop'] = rSinSwTwo.json()[DpidUrl][n]['transmitDropped']
        singleSw [DpidUrl][temp]['pRxDrop'] = rSinSwTwo.json()[DpidUrl][n]['receiveDropped']
        singleSw [DpidUrl][temp]['pColl'] = rSinSwTwo.json()[DpidUrl][n]['collisions']
        singleSw [DpidUrl][temp]['pRxFrEr'] = rSinSwTwo.json()[DpidUrl][n]['receiveFrameErrors']
    for n in range( len(rSFlow.json()[DpidUrl]) ):    #it takes info about FLOWS info
        flow[DpidUrl].append ( {} )
        flow[DpidUrl][n]['fCkie'] = rSFlow.json()[DpidUrl][n]['cookie']    #cookie
        flow[DpidUrl][n]['fPrio'] = rSFlow.json()[DpidUrl][n]['priority']    #priority
        flow[DpidUrl][n]['fPk'] = rSFlow.json()[DpidUrl][n]['packetCount']    #packets number
        flow[DpidUrl][n]['fB'] = rSFlow.json()[DpidUrl][n]['byteCount']    #bytes number
        flow[DpidUrl][n]['fAge'] = rSFlow.json()[DpidUrl][n]['durationSeconds']    #age
        flow[DpidUrl][n]['fTO'] = rSFlow.json()[DpidUrl][n]['idleTimeout']    #timeout
        flow[DpidUrl][n]['fM_src'] = rSFlow.json()[DpidUrl][n]['match']['dataLayerSource']    #match: source
        flow[DpidUrl][n]['fM_dst'] = rSFlow.json()[DpidUrl][n]['match']['dataLayerDestination']    #match: destination
        flow[DpidUrl][n]['fM_port'] = rSFlow.json()[DpidUrl][n]['match']['inputPort']    #match: input port
        flow[DpidUrl][n]['fM_vlan'] = rSFlow.json()[DpidUrl][n]['match']['dataLayerVirtualLan']    #match: vlan
        flow[DpidUrl][n]['fM_prio'] = rSFlow.json()[DpidUrl][n]['match']['dataLayerVirtualLanPriorityCodePoint']    #match: priority
        for m in range ( len(rSFlow.json()[DpidUrl][n]['actions']) ):
            flow[DpidUrl][n]['fA_type'] = []    #it creates a list with "type" of all actions
            flow[DpidUrl][n]['fA_port'] = []    ##it creates a list with "port" of all actions
            flow[DpidUrl][n]['fA_type'].append ( rSFlow.json()[DpidUrl][n]['actions'][m]['type'] )    #action: type
            flow[DpidUrl][n]['fA_port'].append ( rSFlow.json()[DpidUrl][n]['actions'][m]['port'] )    #action: port
    #request.session['switches'] = switches
    #request.session.save()
    request.session.modified = True
    return render (request, 'myfirstapp/SingleSwitch.html', { 'dUrl' : DpidUrl, 'nsSwPort' : singleSw[DpidUrl].keys(),
                                                              'SwInfo' : singleSw[DpidUrl].values(), 
                                                              'flowInfo' : flow[DpidUrl], 'nFlow' : len(flow[DpidUrl]),
                                                              'bugSS' : request.session['switches'],
                                                              'bug1SS' : request.session._session_key } )


