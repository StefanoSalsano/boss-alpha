#view for single switch's informations

from django.shortcuts import render
import requests
import json

def singleSwitch(request, DpidUrl):    #DpidUrl is needed for dinamic url request
    rSinSwOne = requests.get ( 'http://localhost:8080/wm/core/switch/'+DpidUrl+'/features/json' )    #I RestApi
    rSinSwTwo = requests.get ( 'http://localhost:8080/wm/core/switch/'+DpidUrl+'/port/json' )    #II RestApi
    singleSw = {}    #dictionary that contains info about single switch. The key is the switch dpid
    singleSw [DpidUrl] = {}
    for n in range( len(rSinSwOne.json()[DpidUrl]['ports']) ):    #info from first restapi
        temp = rSinSwOne.json()[DpidUrl]['ports'][n]['portNumber']    #it needed to use the port number as a key
        singleSw [DpidUrl] [temp] = {}    #it creates the port number as a key
        singleSw [DpidUrl] [temp]['pName'] = rSinSwOne.json()[DpidUrl]['ports'][n]['name']
        tempT = rSinSwOne.json()[DpidUrl]['ports'][n]['state']
        if tempT == 0:    #to change state info 0 with up and 1 with down 
            singleSw [DpidUrl][temp]['pState'] = 'UP'
        else:
            singleSw [DpidUrl][temp]['pState'] = 'DOWN'
        singleSw [DpidUrl] [temp]['pMac'] = rSinSwOne.json()[DpidUrl]['ports'][n]['hardwareAddress']
    for n in range( len(rSinSwTwo.json()[DpidUrl]) ):    #info from second restapi
        temp = rSinSwTwo.json()[DpidUrl][n]['portNumber']
        singleSw [DpidUrl][temp]['pTxB'] = rSinSwTwo.json()[DpidUrl][n]['transmitBytes']
        singleSw [DpidUrl][temp]['pRxB'] = rSinSwTwo.json()[DpidUrl][n]['receiveBytes']
        singleSw [DpidUrl][temp]['pTxP'] = rSinSwTwo.json()[DpidUrl][n]['transmitPackets']
        singleSw [DpidUrl][temp]['pRxP'] = rSinSwTwo.json()[DpidUrl][n]['receivePackets']
        singleSw [DpidUrl][temp]['pTxDrop'] = rSinSwTwo.json()[DpidUrl][n]['transmitDropped']
        singleSw [DpidUrl][temp]['pRxDrop'] = rSinSwTwo.json()[DpidUrl][n]['receiveDropped']
        singleSw [DpidUrl][temp]['pColl'] = rSinSwTwo.json()[DpidUrl][n]['collisions']
        singleSw [DpidUrl][temp]['pRxFrEr'] = rSinSwTwo.json()[DpidUrl][n]['receiveFrameErrors']
    return render (request, 'myfirstapp/SingleSwitch.html', { 'dUrl' : DpidUrl, 'nsSwPort' : singleSw[DpidUrl].keys(),
                                                              'SwInfo' : singleSw[DpidUrl].values(), } )