from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils.timezone import now

from .models import *

@login_required
def home(request):
    return redirect(reverse('world_map_main', kwargs={'world_map_id':request.user.world_map.pk}))

@login_required
def main(request, world_map_id):
    world_map = get_object_or_404(WorldMap, id=world_map_id)
    terrain = Terrain.objects.all()
    request.user.here_since = now()
    request.user.save(update_fields=['here_since',])
    return render(request, 'world_map/main.html', locals())