#view to show loaded modules

from django.shortcuts import render
import requests
import json

def LoadedMod (request):
    rMod = requests.get ( 'http://localhost:8080/wm/core/module/loaded/json' )
    return render ( request, 'myfirstapp/LoadMod.html', {'lMod' : rMod.json().keys(),
                                                         'nMod' : len(rMod.json()), } )
