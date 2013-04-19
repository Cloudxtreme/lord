from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^attack_player.go$', 'players.views.attack_player', name='players_attack_player'),
    url(r'^login.html$',  'django.contrib.auth.views.login', name="login"),
    url(r'^logout.html$', 'django.contrib.auth.views.logout', name="logout"),
    url(r'^move.go$', 'players.views.move_player', name='players_move_player'),
    url(r'register.html', 'players.views.register', name='register'),
)
