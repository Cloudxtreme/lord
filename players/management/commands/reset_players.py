from django.core.management.base import BaseCommand
from django.db.models import F
from players.models import Player

import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    args = ''
    help = 'Run at daily at midnight to reset all players.'

    def handle(self, *args, **options):
        logger.info('resetting {count} players.'.format(count=len(Player.objects.all())))
        Player.objects.all().update(
            dead=False, 
            hit_points=F('hit_points_max'), 
            fights_left=Player().MAX_FIGHTS, 
            human_fights_left=Player().MAX_HUMAN_FIGHTS,
            seen_bard = False,
            seen_dragon = False,
            seen_master = False,
            seen_violet = False,
            weird_event = False,
            done_special = False,
            flirted = False
        )