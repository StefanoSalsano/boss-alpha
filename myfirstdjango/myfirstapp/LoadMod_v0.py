#view to show loaded modules

from django.shortcuts import render
import requests
import json

def LoadedMod (request):
    rMod = requests.get ( 'http://localhost:8080/wm/core/module/loaded/json' )
    lMod = []    #LIST that contains all loaded modules (without the dependencies)
    for n in range ( len(rMod.json().keys()) ):
        lMod.append ( rMod.json().keys()[n] )
        return render ( request, 'myfirstapp/loadedModules.html', {'lMod' : lMod.keys(),
                                                                   'nMod' : len(lmod) } )
