#!/usr/bin/env python 

from django.shortcuts import render
from myfirstapp.models import Poll
import requests
import json
import string    #module to manipolate the string

#request_SingleSwitchOne 
#restapi_SingleSwitchOne 
#listSplitting (splitted list) each element is a little part of the rest api

def singleSwitch1(request):
    listNumP = {}
    listNameP = {}
    listStatusP = {}
    listTxBP = {}
    listRxBP = {}
    listTxPP = {}
    listRxPP = {}
    listTxDP = {}
    listRxDP = {}
    listFEP = {}
    listMacP = {}
    listCP = {}
    r_SSwOne = requests.get ( 'http://localhost:8080/wm/core/switch/11:11:11:11:11:11:11:11/port/json' )    #request One that contains the info about single switch
    ra_SSwOne = []    #list where we will append the rest api One
    ra_SSwOne.append ( json.dumps(r_SSwOne.json(), sort_keys = False, indent = 4) )    #one element with all RestApi One in json form
    listSplit_SSwOne = string.split ( ra_SSwOne[0], "{" )
    del listSplit_SSwOne[1]    #it deletes the dpid
    del listSplit_SSwOne[0]    #it deletes a space
    i = 0    #index for the name of the dictionary's index
    n = 0    #index to scroll the block of the rest api (each block contains the information about one port)
    while n<len(listSplit_SSwOne):    #to put in infoSwitch_1 the wanted informations
        listInfo_SSw = string.split ( listSplit_SSwOne[n], "," )    #it splits the port's block in a temporary list (listInfo_SSw)
        for scroll in range(len(listInfo_SSw)):
            x = string.find ( listInfo_SSw[scroll], "portNumber")
            if x>0:
                temp = "port_"+str(i)    #it creates the key's name in automatic mode
                a = []
                a.append ( listInfo_SSw[scroll].replace ( "\"", "" ) )    #it deletes "
                a[0] = a[0].replace ( "portNumber:", "" )    #it deletes the written portNumber
                a[0] = a[0].replace ( " ", "" )    #it deletes the space
                listNumP[temp] = a[0]
                print listNumP[temp]
                a.append ( listInfo_SSw[scroll-5] )
                a[1] = a[1].replace ( "\"", "" )
                a[1] = a[1].replace ( "transmitBytes:", "" )
                a[1] = a[1].replace ( " ", "" )    #it deletes the space
                listTxBP[temp] = a[1]
                a.append ( listInfo_SSw[scroll-6] )
                a[2] = a[2].replace ( "\"", "" )
                a[2] = a[2].replace ( "receiveBytes:", "" )
                a[2] = a[2].replace ( " ", "" )    #it deletes the space
                listRxBP[temp] = a[2]
                a.append ( listInfo_SSw[scroll+2] )
                a[3] = a[3].replace ( "\"", "" )
                a[3] = a[3].replace ( "transmitPackets:", "" )
                a[3] = a[3].replace ( " ", "" )    #it deletes the space
                listTxPP[temp] = a[3]
                a.append ( listInfo_SSw[scroll-1] )
                a[4] = a[4].replace ( "\"", "" )
                a[4] = a[4].replace ( "receivePackets:", "" )
                a[4] = a[4].replace ( " ", "" )    #it deletes the space
                listRxPP[temp] = a[4]
                a.append ( listInfo_SSw[scroll+1] )
                a[5] = a[5].replace ( "\"", "" )
                a[5] = a[5].replace ( "receiveFrameErrors:", "" )
                a[5] = a[5].replace ( " ", "" )    #it deletes the space
                listFEP[temp] = a[5]
                a.append ( listInfo_SSw[scroll-2] )
                a[6] = a[6].replace ( "\"", "" )
                a[6] = a[6].replace ( "collisions:", "" )
                a[6] = a[6].replace ( " ", "" )    #it deletes the space
                listCP[temp] = a[6]
                a.append ( listInfo_SSw[scroll-4] )
                a[7] = a[7].replace ( "\"", "" )
                a[7] = a[7].replace ( "transmitDropped:", "" )
                a[7] = a[7].replace ( " ", "" )    #it deletes the space
                listTxDP[temp] = a[7]
                a.append ( listInfo_SSw[scroll-9] )
                a[8] = a[8].replace ( "\"", "" )
                a[8] = a[8].replace ( "receiveDropped:", "" )
                a[8] = a[8].replace ( " ", "" )    #it deletes the space
                listRxDP[temp] = a[8]
                i = i+1
        n = n+1
    r_SSwTwo = requests.get ( 'http://localhost:8080/wm/core/switch/11:11:11:11:11:11:11:11/features/json' )    #request Two
    ra_SSwTwo = []    #list where we will append the rest api Two
    ra_SSwTwo.append ( json.dumps(r_SSwTwo.json(), sort_keys = False, indent = 4) )    #one element with all RestApi Two in json form
    listSplit_SSwTwo = string.split ( ra_SSwTwo[0], "{" )
    del listSplit_SSwTwo[2]    #it deletes the not needed info (the same thing for the two next rows)
    del listSplit_SSwTwo[1]
    del listSplit_SSwTwo[0]
    i = 0    #index for the name of the dictionary's index
    n = 0    #index to scroll the block of the rest api (each block contains the information about one port)
    while n<len(listSplit_SSwTwo):    #to put in infoSwitch_1 the wanted informations from rest api with argument "features"
        listInfo_SSw = string.split ( listSplit_SSwTwo[n], "," )    #it splits the port's block in a temporary list (listInfo_SSw)
        for scroll in range(len(listInfo_SSw)):
            x = string.find ( listInfo_SSw[scroll], "portNumber")
            if x>0:    #it true whether it has found the string with portNumber 
                temp = "port_"+str(i)    #it creates the key's name in automatic mode
                a = []
                a.append ( listInfo_SSw[scroll].replace ( "\"", "" ) )    #it deletes "
                a[0] = a[0].replace ( "portNumber:", "" )    #it deletes the written portNumber
                a[0] = a[0].replace ( " ", "" )    #it deletes the space
                if a[0] == listNumP[temp]:    #it check if port number match with one contained in infoSwitch_1
                    a.append ( listInfo_SSw[scroll-4] )    #it is the switch's name It's serv[9]
                    a[1] = a[1].replace ( "\"", "" )
                    a[1] = a[1].replace ( " ", "" )
                    a[1] = a[1].replace ( "name:", "" )
                    listNameP[temp] = a[1]
                    a.append ( listInfo_SSw[scroll+1] )    #it is the MAC It's serv[10]
                    a[2] = a[2].replace ( "\"", "" )
                    a[2] = a[2].replace ( " ", "" )
                    a[2] = a[2].replace ( "hardwareAddress:", "" )
                    listMacP[temp] = a[2]
                    a.append ( listInfo_SSw[scroll-1] )    #it is the state It's serv[11]
                    a[3] = a[3].replace ( "\"", "" )
                    a[3] = a[3].replace ( " ", "" )
                    a[3] = a[3].replace ( "state:", "" )
                    listStatusP[temp] = a[3]
                    if int(a[3]) == 0:
                        a.append ( "UP" )
                    else:
                        a.append ( "DOWN" )
                    listStatusP[temp] = a[4]
                i = i+1
        n = n+1
    return render (request, 'myfirstapp/singleSwitch1.html', {'NumP_SSw1' : listNumP.values(),
                                                              'NameP_SSw1' : listNameP.values(),
                                                              'StatusP_SSw1' : listStatusP.values(),
                                                              'TxBP_SSw1' : listTxBP.values(),
                                                              'RxBP_SSw1' : listRxBP.values(),
                                                              'TxPP_SSw1' : listTxPP.values(),
                                                              'RxPP_SSw1' : listRxPP.values(),
                                                              'TxDP_SSw1' : listTxDP.values(),
                                                              'RxDP_SSw1' : listRxDP.values(),
                                                              'FEP_SSw1' : listFEP.values(),
                                                              'MacP_SSw1' : listMacP.values(),
                                                              'CP_SSw1' : listCP.values(), } )











