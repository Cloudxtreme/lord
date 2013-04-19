from django.template.loader import render_to_string
from tastypie.authorization import ReadOnlyAuthorization
from tastypie.authentication import SessionAuthentication
from tastypie.exceptions import Unauthorized
from tastypie.resources import ModelResource
from .models import ActivityLog

class ActivityLogAuthorization(ReadOnlyAuthorization):
    def read_list(self, object_list, bundle):
        # This assumes a ``QuerySet`` from ``ModelResource``.
        
        return object_list.filter(to_player=bundle.request.user)

    def read_detail(self, object_list, bundle):
        # Is the requested object owned by the user?
        return bundle.obj.to_player == bundle.request.user
    

class ActivityLogResource(ModelResource):
    class Meta:
        queryset = ActivityLog.objects.all()
        resource_name = 'players/activity_log'
        authentication = SessionAuthentication()
        authorization = ActivityLogAuthorization()
        allowed_methods = ['get',]
        ordering = ['-pk']
        fields = ['id','activity_type','from_player','viewed']
        
    def dehydrate(self, bundle):
        bundle.data['html'] = render_to_string('player/activity_log_entry.html', {'activity':bundle.obj}).replace("\t","").replace("\n", "")
        return bundle
