from django.contrib import admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render_to_response

from .models import *

world_map = models.ForeignKey('MapSquare')
x = models.SmallIntegerField()
y = models.SmallIntegerField()

terrain = models.ForeignKey('Terrain')
battle_odds = models.IntegerField() # how likely will a battle occur?
safe = models.BooleanField(default=False) # can players fight here or not?


class MapSquareAdmin(admin.ModelAdmin):
    list_display = ('world_map','x','y','terrain','battle_odds','safe')
    list_editable = ('terrain', 'battle_odds', 'safe')
    list_filter = ('world_map', 'terrain')

    class Meta:
        model = MapSquare
        
admin.site.register(MapSquare, MapSquareAdmin)

class TerrainAdmin(admin.ModelAdmin):
    list_display = ('name','fg_color','bg_color','character','turns','passable')
    list_editable = ('fg_color','bg_color','character','turns','passable')

    class Meta:
        model = Terrain

admin.site.register(Terrain, TerrainAdmin)

class WorldMapAdmin(admin.ModelAdmin):
    list_display = ('name', 'level_min', 'x_size', 'y_size', 'map_editor_url')
    list_editable = ('level_min', 'x_size', 'y_size')
    readonly_fields = ('map_editor_url',)
    
    class Meta:
        model = WorldMap

@staff_member_required
def world_map_editor(request, world_map_id=None):
    if world_map_id is None:
        raise ValueError('no map selected.')

    terrain = Terrain.objects.all()
    world_map = WorldMap.objects.get(pk=world_map_id)
    return render_to_response('admin/world_map.html', locals())
    
    
admin.site.register(WorldMap, WorldMapAdmin)