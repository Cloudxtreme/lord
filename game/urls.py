from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from players.api import ActivityLogResource
activity_log_resource = ActivityLogResource()

admin.autodiscover()

urlpatterns = patterns('',
    # API URLs
    url(r'^api/', include(activity_log_resource.urls)),
    
    url(r'^world/', include('world.urls')),
    url(r'^players/', include('players.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^.*$', 'world.views.home', name='home'),
)

urlpatterns += staticfiles_urlpatterns()