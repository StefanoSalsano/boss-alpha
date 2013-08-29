from django.shortcuts import render
from myfirstapp.models import Poll
import requests
import json



def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
#    t = loader.get_template('myfirstapp/index.html')
#    c = Context({
#        'latest_poll_list': latest_poll_list,
#    })
    context = { 'latest_poll_list': latest_poll_list, }
#    return HttpResponse(t.render(c))
    return render (request, 'myfirstapp/index.html', context)
#    return HttpResponse("Hello, world. You're at the poll index.")

def info(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]

    r = requests.get('http://localhost:8080/wm/core/controller/switches/json')
    #json_data = r.json()

    a = []
    a.append( json.dumps(r.json(), sort_keys = False, indent = 4))

    context = { 'pluto': a, }
    return render (request, 'myfirstapp/index.html', context)


def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
