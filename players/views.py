from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
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
            new_user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request, new_user)
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
    
    defender = Player.objects.get(id=request.POST['player_id'])
    try:
        attacker_fight_description, defender_fight_description = request.user.attack_player(defender)
        
        # send a message to the attacker about the fight.
        request.user.add_activity_log(
            from_player=defender, 
            activity_type="pvp_attacker",
            message=attacker_fight_description
        )
        
        # send a message to the defender about the fight.
        defender.add_activity_log(
            from_player=request.user, 
            activity_type="pvp_defender",
            message=defender_fight_description
        )
                
    except InvalidAttackException as e: # Cannot attack.
        messages.error(request, e)
    except PlayerDeadException as e: # You are dead.
        messages.error(request, e)
        
    return redirect(return_url)

@login_required
def player_detail(request, player_handle):
    player = Player.objects.get(handle=player_handle)
    return render(request, 'player/detail.html', {'player':player})