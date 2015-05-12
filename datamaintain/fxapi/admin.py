from django.contrib import admin
import models
from forms import ClientAdminForm


class ActionAdmin(admin.ModelAdmin):
    list_display = ('key', 'name', 'action_path','action_permission')
    list_filter = ['action_permission']
    search_fields = ['key', 'name', 'action_path']
    # readonly_fields = ('key','action_path')
    pass

class ClientAdmin(admin.ModelAdmin):
    # form = ClientAdminForm
    list_display = ('user', 'name', 'domain', 'access_key', 
        'access_secret', 'actions')
    list_filter = ['domain','actions','user']
    search_fields = ['name', 'domain', 'access_key', 'user__email']
    filter_vertical = ('actions',)
    pass


admin.site.register(models.Action, ActionAdmin)
admin.site.register(models.Client, ClientAdmin)