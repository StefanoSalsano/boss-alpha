# Goal: to show the RestApi loaded



from django.shortcuts import render
from myfirstapp.models import Poll
import requests
import json
import string    #module to manipolate the string

def LoadedMod (request):
    r_Modules = requests.get ( 'http://localhost:8080/wm/core/module/loaded/json' )
    ra_Modules = []
    ra_Modules.append ( json.dumps(r_Modules.json(), sort_keys = False, indent = 4) )    #one element with whole RestApi in json form
    splitModules = ( string.split(ra_Modules[0], ",") )    #it contains the rest api about loaded modules splitted. It is a LIST
    n = 0
    listModules = []    #it LIST contains the loaded modules
    while n < len(splitModules):    #it parses each element of the listModules
        splitModules[n] = splitModules[n].replace ( "\"", "" )
        x = string.find ( splitModules[n], "loaded: true" )
        if x > 0:
            splitModules[n] = splitModules[n].replace ( "{", "" )
            splitModules[n] = splitModules[n].replace ( "}", "" )
            splitModules[n] = splitModules[n].replace ( "loaded: true", "" )
            listModules.append ( splitModules[n] )
        n= n+1
    nMod = len(listModules)
    return render ( request, 'myfirstapp/loadedModules.html', {'lMod' : listModules } )
