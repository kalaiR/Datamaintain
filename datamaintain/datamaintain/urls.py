from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# from django_cron import models



# from rest_framework import routers
from datamaintain.views import *
admin.autodiscover()

# import django_cron
# django_cron.autodiscover()


# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'absentlist', views.AbsentListViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'datamaintain.views.home', name='home'),
    url(r'^student_admission/$', 'datamaintain.views.student_admission', name='student_admission'), 
#     url(r'^datamaintain/', include('datamaintain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^student_admission/$', 'datamaintain.views.student_admission', name='student_admission'),
    url(r'^create_attendance/$', 'datamaintain.views.create_attendance', name='create_attendance'),
    url(r'^create_excel/$', 'datamaintain.views.create_excel', name='create_excel'),
#     url(r'^display_absent_list/$', 'datamaintain.views.display_absent_list', name='display_absent_list'),
    url(r'^view_attendance/$', 'datamaintain.views.view_attendance', name='view_attendance'),
    url(r'^get_absent_list/$', 'datamaintain.views.get_absent_list', name='get_absent_list'),
    
    url(r'^(?i)admin/card/', include('card.urls')),
    
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^(?i)apidocs/', include('fxapi.urls')),
    url(r'^logout/$', 'datamaintain.views.logout_view', name='logout_view'),
    url(r'^Staff_Details/$', 'datamaintain.views.Staff_Details', name='Staff_Details'), 
    url(r'^Parent_Details/$', 'datamaintain.views.Parent_Details', name='Parent_Details'),
    
)
from datamaintain.api import (AbsentList_RestAPI)

urlpatterns += AbsentList_RestAPI.urls()

