import json
import logging
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls import patterns, url
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models.query import QuerySet
from django.db import models as dj_models
from django.db.models.fields.files import ImageFieldFile, FieldFile
# from fixido.util import check_moderation

from .models import  Client

# logger = logging.getLogger('fixidoapilog')

class RestJSONEncoder(DjangoJSONEncoder):
  print "RestJSONEncoder"
  def default(self, o):
    print "default"
    if isinstance(o, dj_models.Model):
      return dict((k,v) for k,v in vars(o).iteritems() if not k.startswith('_'))
    elif isinstance(o, QuerySet):
      return list(o.values())
    elif isinstance(o, FieldFile):
      if not o:
        return None
      return o.url
    else:      
      return super(RestJSONEncoder, self).default(o)

@csrf_exempt
def handler(request, action, cls, pk=None):
  print "handler"
  method = getattr(cls, 'action_'+action)  
  result = {'status':False, 'data':None, 'error':[]}
  print result
  
  if callable(method):
    args = [request]
    kwargs = {}
    if pk:
      kwargs['pk'] = pk

    try:
      result = method(*args, **kwargs)
      print result
    except Exception as e:
      result['error'].append('Error while doing your action.')
      result['error'].append(e.__str__())
      result['status'] = False
  else:
    result['error'].append('No action found')

  jsback = request.GET.get('jsoncallback', '')
  mimetype = 'application/javascript'
  #print 'REST RESULT', result
  try:
    data =  json.dumps(result, cls=RestJSONEncoder)
  except Exception as e:

    result['error'].append('Error while doing operation.')
    result['error'].append(e.__str__())
    result['status'] = False
    result['data'] = None

    data =  json.dumps(result, cls=RestJSONEncoder)

  # if result['error']:
  #   logger.warning(result['error'])

  if jsback != '':
    data = ("%s(%s)") % (jsback, data)
         
  return HttpResponse(data,mimetype)
     

class RestView(object):
  print "RestView"
  name = ''
  urlprefix = 'api/'

  fields = []
  exclude_fields = []#['keywords']
  extra_fields = []
  safe_fields = []

  model_list_fields = []
  models_list_exclude_fields = []

  model_edit_fields = []
  models_edit_exclude_fields = ['id']

  extra_list_fields = []
  extra_edit_fields = []

  query_fields = []

  model = None
  max_list = 2000
#   actions = ['list', 'get', 'create', 'update', 'delete', 'buy']
  actions = ['list']
  default_filter = None
  filter_by_user = None

  @classmethod
  def create(cls, name, model, model_list_fields=None, model_edit_fields=None, filter_by_user=None, actions=None):
    print "create"
    class Wrap(cls):
      pass

    Wrap.name = name
    Wrap.model = model
    Wrap.model_list_fields = model_list_fields if model_list_fields else []
    Wrap.model_edit_fields = model_edit_fields if model_edit_fields else []
    Wrap.filter_by_user = filter_by_user
    if actions:
      Wrap.actions = actions

    return Wrap

  @classmethod
  def register(cls, name, model, model_list_fields=None, model_edit_fields=None, filter_by_user=None, actions=None):
    print "register"
    wrap = cls.create(name, model, model_list_fields, model_edit_fields, filter_by_user, actions)
    return wrap.urls()

  @classmethod
  def urls(wrap):
    print "urls"

    urls = []
    prefix = r'^(?i)' + wrap.urlprefix  + wrap.name + '/'


    for action in wrap.actions:
      if action in 'list':
        urlname = '_'.join(['api', wrap.name, action])
        urls.append((prefix+r'list/$', handler, {'cls':wrap, 'action':'list'}))

      elif action in 'create':
        urlname = '_'.join(['api', wrap.name, action])
        urls.append((prefix+r'create/$', handler, {'cls':wrap, 'action':'create'}))

      elif action in 'update':
        urlname = '_'.join(['api', wrap.name, action])
        urls.append((prefix+r'update/(?P<pk>\d+)/$', handler, {'cls':wrap, 'action':'update'}))

      elif action in 'delete':
        urlname = '_'.join(['api', wrap.name, action])
        urls.append((prefix+r'delete/(?P<pk>\d+)/$', handler, {'cls':wrap, 'action':'delete'}))
    
      # elif action in 'buy':
      #   urlname = '_'.join(['api', wrap.name, action])
      #   urls.append((prefix+r'buy/(?P<pk>\d+)/$', handler, {'cls':wrap, 'action':'buy'}))


      # elif action in 'get':
      #   urlname = '_'.join(['api', wrap.name, action])
      #   urls.append((prefix+r'get/(?P<pk>\d+)/$', handler, {'cls':wrap, 'action':'get'}))


    return patterns('', *urls)

  @classmethod
  def validate(cls, request, action, check_for_seller=False):
    print "validate"
    action = '-'.join([cls.name, action])
    if 'access_key' in request.REQUEST \
      and 'access_secret' in request.REQUEST:
      print request.REQUEST['access_key']
      print request.REQUEST['access_secret']
      access_key = request.REQUEST['access_key']
      access_secret = request.REQUEST['access_secret']
      (access, user) = Client.have_access(access_key, access_secret, action)
      print '1', access
      print '2', user
      print '3', action

      return (access, user)

    return (False, None)
  
  @classmethod
  def get_all_model_fields(cls):
    print "get_all_model_fields"
    #fields = cls.fields if cls.fields else cls.model._meta.get_all_field_names()
    fields = cls.fields if cls.fields else [f.attname for f in cls.model._meta.local_fields]
    return fields

  @classmethod
  def get_model_list_fields(cls,pk=None):
    print "get_model_list_fields"
    return list(set(cls.model_list_fields) - set(['reference']))

    # if cls.model_list_fields:
    #   print cls.model_list_fields  
    #   print "2", pk
    #   if pk == None:
    #       print "Enter with pk"
    #       return list(set(cls.model_list_fields) - set(['reference']))
    #   else: 
    #       print "Enter"
    #       return cls.model_list_fields

    # elif cls.models_list_exclude_fields:
    #   fields = cls.get_all_model_fields()
    #   return list(set(fields) - set(cls.models_list_exclude_fields))

    # return cls.get_all_model_fields()


  @classmethod
  def get_model_edit_fields(cls):
    print "get_model_edit_fields"
    if cls.model_edit_fields:
      return cls.model_edit_fields

    elif cls.models_edit_exclude_fields:
      fields = cls.get_all_model_fields()
      return list(set(fields) - set(cls.models_edit_exclude_fields))

    return cls.get_all_model_fields()

  @classmethod
  def get_all_edit_fields(cls):
    print "get_all_edit_fields"
    return cls.get_model_edit_fields() + cls.extra_edit_fields

  @classmethod
  def get_valid_fields(cls):
    print "get_valid_fields"
    fields = cls.fields if cls.fields else cls.model._meta.get_all_field_names()
    if cls.exclude_fields:
      return list(set(fields) - set(cls.exclude_fields))
    return fields

  @classmethod
  def action_list(cls, request, limit=None, pk=None, action='list', 
    is_buyer=False):
    print "action_list"
    print "3", pk
    # if is_buyer:
    #   cls.filter_by_user = None

    access, user = cls.validate(request, action)
    print access
    print user
    print "action_list pk", pk
    result = {'status':False, 'data':None, 'error':[]}

    if access:
      if cls.model or cls.default_filter:

        if pk:
          try:
            kwargs = {'pk':pk}
            if cls.filter_by_user:
              kwargs[cls.filter_by_user] = user
            
            data = cls.model.objects.get(**kwargs)
          except Exception as e:
            data = None
            #result['error'].append(e.__str__())
            #result['error'].append("Data not found for id: %s"%pk)
            result['error'].append("You are not authorised for this action")

        else:

          data = cls.model.objects.order_by('-id')

          if cls.default_filter is not None:
            data = cls.default_filter

          if cls.filter_by_user:
            kwargs = {}
            kwargs[cls.filter_by_user] = user
            data = data.filter(**kwargs)

          if limit:
            data = data[0:limit]

          if limit == 1:
            if data.count() > 0:
              data = data.get()
            else:
              data = None
          elif limit is None:
            data = data[0:cls.max_list]

          if data and limit != 1:
            #print 'DATA', data, cls.get_model_list_fields()
            data = data.values(*cls.get_model_list_fields(pk))

        result['data'] = data
        if data:
          result['status'] = True

    else:
      result['error'].append("You don't have accesss to it")

    # if result['error']:
    #   logger.warning(result['error'])

    return result

  @classmethod
  def action_update(cls, request, pk=None):
    print "action_update"
    print "1", pk
    access, user = cls.validate(request, 'list')
    seller_access, user = cls.validate(request, 'list', check_for_seller=True)
    result = {'status':False, 'data':None, 'error':[]}
    action = 'update' if pk else 'create'

    if not access:
      result['error'].append("You don't have access to it!")
      # logger.warning(result['error'])
      return result
    
    if not seller_access:
      result['error'].append("You are not a seller to create a lead!")
      # logger.warning(result['error'])
      return result

    if cls.model:
      data = cls.model()

      if pk:
        list_result = cls.action_list(request, pk=pk, action=action)
        if not list_result['status']:
          return list_result
        if not list_result['data']:
          result['error'].append('Item not found ')
          # logger.warning(result['error'])
          return result

        data = cls.model.objects.get(pk=pk)

      fields = cls.get_model_edit_fields()

      for field in fields:
        if field in request.POST and request.POST[field]:
          #TODO: Do validation based on field type
          setattr(data, field, request.POST[field])
        if field in request.FILES:
          filedata = request.FILES[field]
          if filedata:
            setattr(data, field, filedata)

      if cls.filter_by_user:
        setattr(data, cls.filter_by_user, user)

      if check_moderation() and action == 'create':
        setattr(data, 'active', False)
        setattr(data, 'inactive_reason', 'moderate')

      data.save()

      data = data.pk
      result['data'] = data
      result['status'] = True

    return result

  @classmethod
  def action_create(cls, request):
    print "action_create"
    return cls.action_update(request)

  @classmethod
  def action_get(cls, request, pk):
    print "action_get"
    return cls.action_list(request, pk=pk, action='get')

  @classmethod
  def action_buy(cls,request,pk):
   print "action_buy"
   return cls.action_list(request, limit, pk=pk, action ='buy')

  @classmethod
  def action_delete(cls, request, pk):
    print "action_delete"
    list_result = cls.action_list(request, pk=pk, action='delete')

    if list_result['status'] and list_result['data']:
      list_result['data'].delete()
      list_result['data'] = list_result['data'].pk

    return list_result


def render_json_response(request, data, status=True):
  print "render_json_response"
  data = json.dumps({'data':data, 'status':status}, cls=RestJSONEncoder)
  return HttpResponse(data, 'application/javascript')
