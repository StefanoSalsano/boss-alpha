# DEBUG view to create the scripting for flows in SingleSwitch

from django.shortcuts import render
import requests
import json

def prova (request):
    pluto = '22:22:22:22:22:22:22:22'
    dpid = unicode(pluto)
    flows = {}
    flows[dpid] = []
    flows[dpid].append ( {} )
    flows[dpid].append ( {} )
    flows[dpid][0]['fA_type'] = []
    flows[dpid][0]['fA_port'] = []
    flows[dpid][1]['fA_type'] = []
    flows[dpid][1]['fA_port'] = []
    flows[dpid][0]['fCkie'] = 'Ckie_1'
    flows[dpid][1]['fCkie'] = 'Ckie_2'
    flows[dpid][0]['fPrio'] = 'prio_1'
    flows[dpid][1]['fPrio'] = 'prio_2'
    flows[dpid][0]['fPk'] = 'pk_1'
    flows[dpid][1]['fPk'] = 'pk_2'
    flows[dpid][0]['fB'] = 'b_1'
    flows[dpid][1]['fB'] = 'b_2'
    flows[dpid][0]['fAge'] = 'age_1'
    flows[dpid][1]['fAge'] = 'age_2'
    flows[dpid][0]['fTO'] = 'to_1'
    flows[dpid][1]['fTO'] = 'to_2'
    flows[dpid][0]['fM_src'] = 'src_1'
    flows[dpid][1]['fM_src'] = 'src_2'
    flows[dpid][0]['fM_dst'] = 'dest_1'
    flows[dpid][1]['fM_dst'] = 'dest_2'
    flows[dpid][0]['fM_vlan'] = 'vlan_1'
    flows[dpid][1]['fM_vlan'] = 'vlan_2'
    flows[dpid][0]['fM_prio'] = 'prio_1'
    flows[dpid][1]['fM_prio'] = 'prio_2'
    flows[dpid][0]['fM_port'] = 'Mport_1'
    flows[dpid][1]['fM_port'] = 'Mport_2'
    flows[dpid][0]['fA_type'].append ('type_1A')
    flows[dpid][0]['fA_type'].append ('type_1B')
    flows[dpid][1]['fA_type'].append ('type_2A')
    flows[dpid][1]['fA_type'].append('type_2B')
    flows[dpid][0]['fA_port'].append('port_1A')
    flows[dpid][0]['fA_port'].append('port_1B')
    flows[dpid][1]['fA_port'].append('port_2A')
    flows[dpid][1]['fA_port'].append('port_2B')
    return render ( request, 'myfirstapp/prova1.html', { 'flowInfo' : flows[dpid] } )



















    