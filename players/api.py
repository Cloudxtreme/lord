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
        # include full html for activity.
        bundle.data['activity_html'] = render_to_string('player/activity_log_entry.html', {'activity':bundle.obj}).replace("\t","").replace("\n", "")
        bundle.data['from_player'] = bundle.obj.from_player.handle
        
        # include hp if activity is a fight.
        if bundle.obj.activity_type in ('pvp_attacker', 'pvp_defender'):
            bundle.data['hit_points'] = bundle.obj.to_player.hit_points
            bundle.data['hp_class'], bundle.data['percent_hp_remaining'] = bundle.obj.to_player.get_hp_status()
            
        
        # if activity is an arrival or departure, then include html needed to add to the nearby players list interface.
        elif bundle.obj.activity_type in ('arrival','departure'):
            bundle.data['other_players_blurb'] = render_to_string('player/other_players_blurb.html', {'player':bundle.obj.to_player})
            if bundle.obj.activity_type == 'arrival':
                bundle.data['other_players_html'] = render_to_string('player/other_player.html', {'player':bundle.obj.from_player})
        return bundle
