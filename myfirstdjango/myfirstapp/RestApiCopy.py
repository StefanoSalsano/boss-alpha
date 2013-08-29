# "django view for RestApi"

from django.shortcuts import render
from myfirstapp.models import Poll
import requests
import json
import string    #module to manipolate the string

def switchesInfo(request):
    rOne = requests.get ( 'http://localhost:8080/wm/core/controller/switches/json' )    #request that contains dpid address port
    restapiOne = []    #list with rOne request
    restapiOne.append ( json.dumps(rOne.json(), sort_keys = False, indent = 4) )    #one element with all RestApi One in json form
    mylistapiOne = string.split ( restapiOne[0], ',' )    #the RestApiOne splitted in the elements of the list
    dpidList = {}    #dictionary that contain all dpid
    addrList = {}    #dictionary where is saved the address
    portList = {}    #dictionary where is saved the port
    i = 0    #index for the name dpid_i
    j = 0    #service index to locate dpid in the mylistapiOne
    for searchdpid in mylistapiOne:    #it save in dpidList (it is a dictionary) all dpid as dpid_0, dpid_1 (they are the dictionary's indexes)
        x = string.find ( searchdpid, "dpid")
        if x>0:
            temp = "dpid_"+str(i)
            a = []
            a.append ( searchdpid.replace ( "\"", "" ) )
            a[0] = a[0].replace ( "dpid:", "" )
            a[0] = a[0].replace ( "\n", "" )
            a[0] = a[0].replace ( " ", "" )    #it delete the space at the beginning
            dpidList[temp] = a[0]
            mylistapiOne[j-2] = mylistapiOne[j-2].replace ( "\"", "" )
            mylistapiOne[j-2] = mylistapiOne[j-2].replace ( ":", " " )
            b = string.split ( mylistapiOne[j-2] )
            addrList[temp] = b[1]
            portList[temp] = b[2]
            i = i+1
        j = j+1
    rTwo = requests.get ( 'http://localhost:8080/wm/core/switch/all/desc/json' )    #manufacturer request
    restapiTwo = []    #list with rTwo request
    restapiTwo.append ( json.dumps(rTwo.json(), sort_keys = False, indent = 4) )    #one element with all RestApi Two
    mylistapiTwo = string.split ( restapiTwo[0], ',' )    #the RestApiTwo splitted in the elements
    manufList = {}    #dictionary with manufacturing informations
    appoggio = []
    j = 0    #index used to scrol the dpid's name eg dpid_0 dpid_1
    while j<len(dpidList):    #it looks for dpid in rTwo and saves the manufacturer information in manufList
        temp = "dpid_"+str(j)
        for index in range ( len(mylistapiTwo) ):    #it look for 
            y = string.find ( mylistapiTwo[index], dpidList[temp] )    #it look the dpid value in mylistapiTwo
            if y>0:    #whether it found the dpid value, the manufaturer info are in position index+3 of mylistapiTwo
                mylistapiTwo[index+3] = mylistapiTwo[index+3].replace ( " \"manufacturerDescription\": \"", "" )
                mylistapiTwo[index+3] = mylistapiTwo[index+3].replace ( "\n", "" )
                mylistapiTwo[index+3] = mylistapiTwo[index+3].replace ( " ", "" )
                manufList[temp] = mylistapiTwo[index+3]
        j=j+1
    r_Hosts = requests.get ( 'http://localhost:8080/wm/device/' )
    ra_Hosts = []
    ra_Hosts.append ( json.dumps(r_Hosts.json(), sort_keys = False, indent = 4) )    #one element with whole RestApi in json form
    listHosts = ( string.split(ra_Hosts[0], "entityClass") )    #each listHosts's element contains info about single host
    del listHosts[0]
    n = 0
    i = 0
    list_HMac = {}    #it contains the host's mac address
    list_HIp = {}    #it contains the host's ip addresss
    list_HSwPort = {}    #it contains the port of the switch where the host is attached
    list_HSwDpid = {}    #it contains the DPID of the switch where the host is attached
    while n < len(listHosts):
        listHosts[n] = listHosts[n].replace ( "{", "" )
        listHosts[n] = listHosts[n].replace ( "}", "" )
        listHosts[n] = listHosts[n].replace ( "[", "" )
        listHosts[n] = listHosts[n].replace ( "]", "" )
        listHosts[n] = listHosts[n].replace ( " ", "" )
        listHosts[n] = listHosts[n].replace ( "\n", "" )
        listSplit_Hosts = string.split( listHosts[n], "," )    #each element contains the info about single host
        for scroll in range(len(listSplit_Hosts)):
            x = string.find ( listSplit_Hosts[scroll], "mac" )
            if x > 0:
                listSplit_Hosts[scroll] = listSplit_Hosts[scroll].replace ( "\"", "" )
                listSplit_Hosts[scroll] = listSplit_Hosts[scroll].replace ( "mac:", "" )
                temp = "mac_"+str(i)    #it creates the key's name in automatic mode
                list_HMac[temp] = listSplit_Hosts[scroll]
                listSplit_Hosts[scroll+1] = listSplit_Hosts[scroll+1].replace ( "\"", "" )
                listSplit_Hosts[scroll+1] = listSplit_Hosts[scroll+1].replace ( "ipv4:", "" )
                list_HIp[temp] = listSplit_Hosts[scroll+1]
                listSplit_Hosts[scroll-1] = listSplit_Hosts[scroll-1].replace ( "\"", "" )
                listSplit_Hosts[scroll-1] = listSplit_Hosts[scroll-1].replace ( "port:", "" )
                list_HSwPort[temp] = listSplit_Hosts[scroll-1]
                listSplit_Hosts[scroll-2] = listSplit_Hosts[scroll-2].replace ( "\"", "" )
                listSplit_Hosts[scroll-2] = listSplit_Hosts[scroll-2].replace ( "switchDPID:", "" )
                list_HSwDpid[temp]= listSplit_Hosts[scroll-2]
                i = i+1
        n = n+1
    return render (request, 'myfirstapp/switches.html', {'dpid' : dpidList.values(), 'port' : portList.values(),
                                                        'addr' : addrList.values(), 'manuf' : manufList.values(),
                                                        'HMac' : list_HMac.values(),
                                                        'HIp' : list_HIp.values(),
                                                        'HSwPort' : list_HSwPort.values(),
                                                        'HSwDpid' : list_HSwDpid.values() } )














