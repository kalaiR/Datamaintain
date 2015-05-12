from django.conf.urls import patterns, url

urlpatterns = patterns('fxapi.views',
	(r'playground/$', 'playground'),
	(r'clients/$', 'clients'),
	(r'docs/$', 'docs'),
	(r'faq/$', 'faq'),
	(r'$', 'index'),
)