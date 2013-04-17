from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
urlpatterns = patterns('',
    url(r'^worldmap/(?P<world_map_id>[0-9]*)/main.html$', 'world.views.main', name='world_map_main'),
    url(r'^worldmap/(?P<world_map_id>[0-9]*)/edit.html$', 'world.admin.world_map_editor', name="world_map_edit")
)
