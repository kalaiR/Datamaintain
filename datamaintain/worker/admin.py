from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from django.http import HttpResponseRedirect
from django.http import HttpResponse, Http404

import models
# from actors.models import Actor

from dateutil import tz
#from_zone = tz.tzutc()
to_zone = tz.tzlocal()

class WorkerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'interval', 'wait_for_approval', 'active')
  list_filter = ['name', 'active']
  search_fields = ['name', 'cls_path', 'interval', 'wait_for_approval', 'active']
  pass

# class WorkerTaskAdmin(admin.ModelAdmin):
#   list_display = ('id', 'worker', 'notes', 'worker_options', 'status', 'completed', 'modified')
#   list_filter = ['worker', 'status']
#   search_fields = ['worker', 'notes', 'worker_options', 'status']
  
#   list_per_page = 100


admin.site.register(models.Worker, WorkerAdmin)
# admin.site.register(models.WorkerTask, WorkerTaskAdmin)

