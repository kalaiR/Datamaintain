from django.conf.urls import patterns, url

urlpatterns = patterns('card.views',
    url(r'^create_attendance/$', 'create_attendance', name='create_attendance'),
    url(r'^staff_create_attendance/$', 'staff_create_attendance', name='staff_create_attendance'),
    url(r'^view_attendance/$', 'view_attendance', name='view_attendance'),
    
)
