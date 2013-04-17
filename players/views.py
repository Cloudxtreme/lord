from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import redirect, render

from .admin import PlayerAddForm
from .models import InvalidAttackException, InvalidMoveException, Player, PlayerDeadException

import logging

logger = logging.getLogger(__name__)

def register(request):
    if request.method == 'POST':
        form = PlayerAddForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = PlayerAddForm()

    return render(request, "registration/register.html", {
        'form': form,
    })
    
@login_required
def move_player(request):
    direction = request.POST['direction']
    try:
        request.user.move(direction)
        request.user.save(update_fields=['world_map','map_square','here_since',])
    except InvalidMoveException as e:
        messages.error(request, e)
    except PlayerDeadException as e:
        messages.error(request, e)
    
    return redirect(reverse('world_map_main', args=(request.user.world_map.pk,)))
    
@login_required
def attack_player(request):
    return_url = reverse('world_map_main', args=(request.user.world_map.pk,))
    
    player = Player.objects.get(id=request.POST['player_id'])
    try:
        fight_description = request.user.attack_player(player)
        if request.user.dead:
            messages.error(request, fight_description)
        else:
            messages.info(request, fight_description)
    except InvalidAttackException as e:
        messages.error(request, e)
    except PlayerDeadException as e:
        messages.error(request, e)
        
    return redirect(return_url)
    
#django.contrib.auth.signals.user_logged_out