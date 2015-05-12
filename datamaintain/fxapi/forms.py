from django import forms
# from actors.models import ActorCampaignEmailStatistics,Note,Actor
from models import Client,Action

action_obj = Action.objects.all()
action_list = []
for i in action_obj:
    action_list.append((str(i.key),str(i.name) +' - ' +str(i.action_permission) ))
    print "action_list", action_list
action_tuple = tuple(action_list)
print "action_tuple", action_tuple

class ClientAdminForm(forms.ModelForm):
    actions = forms.ChoiceField( 
        widget = forms.SelectMultiple(attrs={'size': 12}),
        required = False,
        choices = action_tuple,
    )
    
    class Meta:
        model = Client 