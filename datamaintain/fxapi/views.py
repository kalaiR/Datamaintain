from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
import json
import models
from django.contrib.auth.models import User
from datamaintain.models import *
from fxapi.models import *


# from actors.models import Actor
# from leads.models import LeadCategory

def index(request):
    return render_to_response('fxapi/index.html', context_instance=RequestContext(request))

def docs(request):
    return render_to_response('fxapi/docs.html', context_instance=RequestContext(request))

def faq(request):
    return render_to_response('fxapi/faq.html', context_instance=RequestContext(request))


@login_required
def playground(request):
    import datamaintain.api
    import fxapi
    all_actions = {
        'absentlist': datamaintain.api.AbsentList_RestAPI,         
    }

    context = {}
    user = User.objects.get(pk=request.user.pk)
    absent_list = AbsentList.objects.all()
    context['clients']  = Client.objects.filter(user=user)
    action_fields = {}
    actions ={}

    for client in context['clients'].all():
        actions[client.pk] =  client.actions.all()[:]

    for client_action in actions.values():
        for action in client_action:
            action_fields[action.pk] = {}
            prefix = action.pk.split('-')[0]
            if prefix in all_actions:
                actioncls  = all_actions[prefix]
                vals = {}
                for k in dir(actioncls):
                    v = getattr(actioncls, k)
                    if (not k.startswith('_')) and (not callable(v)):
                        vals[k] = v
                action_fields[action.pk] = vals
                action_fields[action.pk]['valid_fields'] = actioncls.get_valid_fields()
                action_fields[action.pk]['query_fields'] = actioncls.query_fields
                
                action_fields[action.pk]['type'] = action.pk.split('-')[-1]
                #print action_fields[action.pk]['type'], action.pk
                #_fields = set(actioncls.get_valid_fields() + actioncls.extra_fields)
                #_fields = _fields - set(actioncls.safe_fields)
                action_fields[action.pk]['all_fields'] = actioncls.get_all_edit_fields()
                print "absent_list_all_fields", action_fields[action.pk]['all_fields']
                action_fields[action.pk]['action'] = action

    context['actions'] = actions
    print "actions", context['actions']
    context['action_fields'] = action_fields
    print "action_fields", context['action_fields']
    context['absent_list'] = absent_list
    print "absent_list", context['absent_list']
    
    jdata = json.dumps(context, cls=fxapi.RestJSONEncoder)
    context['json'] = jdata
    context['user'] = user

    return render_to_response('fxapi/playground.html', context, context_instance=RequestContext(request))

@login_required
def clients(request):
    context = {}

    user = User.objects.get(pk=request.user.pk)
    context['user'] = user
    context['clients'] = Client.objects.filter(user=user)

    if request.method == "POST" and 'action' in request.POST and \
        request.POST['action'] == 'delete':

        delete_id = request.POST['delete_id']
        Client.objects.filter(pk=delete_id).delete()

    elif request.method == "POST":
        name = request.POST['name']
        domain = request.POST['domain']
        description = request.POST['description']
        client = Client(name=name, user=user, 
            domain=domain, description=description)
        client.save()       
        
        client.actions = Client.default_actions()
        client.save()

    return render_to_response('fxapi/clients.html', context,  context_instance=RequestContext(request))