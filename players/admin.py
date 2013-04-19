from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import *

class PlayerAddForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = Player
        fields = ('email', 'first_name', 'last_name', 'handle', 'gender')
        
    def save(self, commit=True):
        user = super(PlayerAddForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
        
class PlayerChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = Player
        
    def clean_password(self):
        return self.initial['password']

    # Location Info
    world_map = models.ForeignKey(WorldMap, default=1)
    map_square = models.ForeignKey(MapSquare, default=1)
    here_since = models.DateTimeField(auto_now_add=True, default=now)


class PlayerAdmin(admin.ModelAdmin):
    form = PlayerChangeForm
    add_form = PlayerAddForm
    
    list_display = ('email', 'first_name', 'last_name', 'handle', 'last_login', 'created_at', 'modified_at')
    list_filter = ('is_superuser', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Player Info', {'fields': ('handle', 'gender')}),
        ('Vitals', {'fields': ('hit_points', 'hit_points_max','dead','inn','defense','strength','charm','king')}),
        ('Love Life', {'fields': ('lays','married','kids',)}),
        ('Turn Data', {'fields': ('fights_left','human_fights_left','seen_bard','seen_dragon','seen_master','seen_violet','weird_event','done_special','flirted')}),
        ('Inventory', {'fields': ('equipped_armor','equipped_weapon','gold','bank','gem')}),
        ('Skills', {'fields': ('death_knight_level','death_knight_skill','mystical_level','mystical_skill','theif_level','theif_skill')}),
        ('Location', {'fields': ('world_map','map_square',)}),
        ('Permissions', {'fields': ('is_active','is_staff','is_superuser','groups',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'handle', 'password')
        }),
    )
    search_fields = ('email', 'last_name', 'handle')
    filter_horizontal = ()

admin.site.register(Player, PlayerAdmin)

class ArmorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Armor)

class WeaponAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Weapon)

class MonsterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Monster)
