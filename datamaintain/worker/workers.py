import logging
import time
import traceback
import operator
from datetime import datetime, timedelta
from models import *
from django.conf import settings
from django.contrib.sites.models import Site
from datamaintain.models import *
# from actors import globals as glb #couldn't work w/o request

class WorkerBase(object):

  def __init__(self, worker):
    self.worker = worker

  def create_tasks(self):
    pass

  def prepare(self):
    pass

  def runtasks(self, tasks):
    pass

  def finish(self):
    pass

class AttendanceNotificationWorker(WorkerBase):

  def create_tasks(self):
    print 'create_task'
    pass    

  def runtasks(self, tasks):
    print 'runtask'
    year = Year()
    year.year = '6'
    year.save()
    pass