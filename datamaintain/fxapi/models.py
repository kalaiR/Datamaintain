from django.db import models
from django.contrib.auth.models import User

import  core
from core import helper
ACTION_USAGE = (
    ('Internal', 'Internal'),
    ('External', 'External'),
)

class Action(models.Model):
    INTERNAL = 'Internal'
    key = models.CharField(max_length=64, primary_key=True, unique=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    action_path = models.CharField(max_length=512)
    action_permission = models.CharField(max_length=20,choices=ACTION_USAGE,default=INTERNAL)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.__unicode__()

    @staticmethod
    def default_data():
        Action.objects.get_or_create(key='absentlist-list', name="Absent list", action_path='/api/absentlist/list/')
       
        

class Client(models.Model):

    name = models.CharField(max_length=64)
    user = models.ForeignKey(User)
    domain = models.CharField(max_length=128, null=True, blank=True)
    description = models.CharField(max_length=512, null=True, blank=True)
    
    access_key = models.CharField(max_length=265, null=True, blank=True, 
        help_text="Leave it blank, it will generated automatically")
    access_secret = models.CharField(max_length=256, null=True, blank=True, 
        help_text="Leave it blank, it will generated automatically")
    
    #TODO: if there are more actions in future, use ActionGroups
    actions = models.ManyToManyField(Action, null=True)
    active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.access_key:
            self.access_key = helper.randomkey(16)

        if not self.access_secret:
            self.access_secret = helper.randomkey(32)

        super(Client, self).save(*args, **kwargs)

    def __unicode__(self):
        return '-'.join([self.name, str(self.user)])

    def __str__(self):
        return self.__unicode__()

    @classmethod
    def have_access(cls, access_key, access_secret, action):
        print "1", access_key
        print "2",access_secret
        print "3", action
        client = Client.objects.filter(access_key=access_key, 
            access_secret=access_secret, active=True, actions = action)
        
        print "users", client
        
        if client.exists():
            
            client = client[0]
            print "5" , client.actions
#             if check_for_seller:
#                 return (client.user.is_sellerregistered, client.user)
            print "have_access", client.user
            print "have_access1", client.actions
            return (True, client.user)

        return (False, None)
    
    @classmethod
    def default_actions(cls):
        
        return [
            'absentlist-list',
        ]
