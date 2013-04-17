# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Monster'
        db.create_table(u'players_monster', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('strength', self.gf('django.db.models.fields.IntegerField')()),
            ('gold', self.gf('django.db.models.fields.IntegerField')()),
            ('weapon', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['players.Weapon'])),
            ('experience', self.gf('django.db.models.fields.IntegerField')()),
            ('hit_points', self.gf('django.db.models.fields.IntegerField')()),
            ('death', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'players', ['Monster'])

        # Adding model 'Armor'
        db.create_table(u'players_armor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('defense', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'players', ['Armor'])

        # Adding model 'Weapon'
        db.create_table(u'players_weapon', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('price', self.gf('django.db.models.fields.IntegerField')()),
            ('strength', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'players', ['Weapon'])

        # Adding field 'Player.level'
        db.add_column(u'players_player', 'level',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Player.experience'
        db.add_column(u'players_player', 'experience',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.player_kills'
        db.add_column(u'players_player', 'player_kills',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.dead'
        db.add_column(u'players_player', 'dead',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.inn'
        db.add_column(u'players_player', 'inn',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.defense'
        db.add_column(u'players_player', 'defense',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.strength'
        db.add_column(u'players_player', 'strength',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.charm'
        db.add_column(u'players_player', 'charm',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.king'
        db.add_column(u'players_player', 'king',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.lays'
        db.add_column(u'players_player', 'lays',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.married'
        db.add_column(u'players_player', 'married',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['players.Player'], null=True),
                      keep_default=False)

        # Adding field 'Player.kids'
        db.add_column(u'players_player', 'kids',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.fights_left'
        db.add_column(u'players_player', 'fights_left',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.human_fights_left'
        db.add_column(u'players_player', 'human_fights_left',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.seen_bard'
        db.add_column(u'players_player', 'seen_bard',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.seen_dragon'
        db.add_column(u'players_player', 'seen_dragon',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.seen_master'
        db.add_column(u'players_player', 'seen_master',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.seen_violet'
        db.add_column(u'players_player', 'seen_violet',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.weird_event'
        db.add_column(u'players_player', 'weird_event',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.done_special'
        db.add_column(u'players_player', 'done_special',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.flirted'
        db.add_column(u'players_player', 'flirted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Player.equipped_armor'
        db.add_column(u'players_player', 'equipped_armor',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['players.Armor'], null=True),
                      keep_default=False)

        # Adding field 'Player.equipped_weapon'
        db.add_column(u'players_player', 'equipped_weapon',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['players.Weapon'], null=True),
                      keep_default=False)

        # Adding field 'Player.gold'
        db.add_column(u'players_player', 'gold',
                      self.gf('django.db.models.fields.IntegerField')(default=10),
                      keep_default=False)

        # Adding field 'Player.bank'
        db.add_column(u'players_player', 'bank',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.gem'
        db.add_column(u'players_player', 'gem',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.last_alive_time'
        db.add_column(u'players_player', 'last_alive_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, auto_now_add=True, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Player.last_dead_time'
        db.add_column(u'players_player', 'last_dead_time',
                      self.gf('django.db.models.fields.DateTimeField')(default=None, null=True),
                      keep_default=False)

        # Adding field 'Player.days_played'
        db.add_column(u'players_player', 'days_played',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.death_knight_level'
        db.add_column(u'players_player', 'death_knight_level',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.death_knight_skill'
        db.add_column(u'players_player', 'death_knight_skill',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.mystical_level'
        db.add_column(u'players_player', 'mystical_level',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.mystical_skill'
        db.add_column(u'players_player', 'mystical_skill',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.theif_level'
        db.add_column(u'players_player', 'theif_level',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'Player.theif_skill'
        db.add_column(u'players_player', 'theif_skill',
                      self.gf('django.db.models.fields.SmallIntegerField')(default=0),
                      keep_default=False)


        # Changing field 'Player.created_at'
        db.alter_column(u'players_player', 'created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):
        # Deleting model 'Monster'
        db.delete_table(u'players_monster')

        # Deleting model 'Armor'
        db.delete_table(u'players_armor')

        # Deleting model 'Weapon'
        db.delete_table(u'players_weapon')

        # Deleting field 'Player.level'
        db.delete_column(u'players_player', 'level')

        # Deleting field 'Player.experience'
        db.delete_column(u'players_player', 'experience')

        # Deleting field 'Player.player_kills'
        db.delete_column(u'players_player', 'player_kills')

        # Deleting field 'Player.dead'
        db.delete_column(u'players_player', 'dead')

        # Deleting field 'Player.inn'
        db.delete_column(u'players_player', 'inn')

        # Deleting field 'Player.defense'
        db.delete_column(u'players_player', 'defense')

        # Deleting field 'Player.strength'
        db.delete_column(u'players_player', 'strength')

        # Deleting field 'Player.charm'
        db.delete_column(u'players_player', 'charm')

        # Deleting field 'Player.king'
        db.delete_column(u'players_player', 'king')

        # Deleting field 'Player.lays'
        db.delete_column(u'players_player', 'lays')

        # Deleting field 'Player.married'
        db.delete_column(u'players_player', 'married_id')

        # Deleting field 'Player.kids'
        db.delete_column(u'players_player', 'kids')

        # Deleting field 'Player.fights_left'
        db.delete_column(u'players_player', 'fights_left')

        # Deleting field 'Player.human_fights_left'
        db.delete_column(u'players_player', 'human_fights_left')

        # Deleting field 'Player.seen_bard'
        db.delete_column(u'players_player', 'seen_bard')

        # Deleting field 'Player.seen_dragon'
        db.delete_column(u'players_player', 'seen_dragon')

        # Deleting field 'Player.seen_master'
        db.delete_column(u'players_player', 'seen_master')

        # Deleting field 'Player.seen_violet'
        db.delete_column(u'players_player', 'seen_violet')

        # Deleting field 'Player.weird_event'
        db.delete_column(u'players_player', 'weird_event')

        # Deleting field 'Player.done_special'
        db.delete_column(u'players_player', 'done_special')

        # Deleting field 'Player.flirted'
        db.delete_column(u'players_player', 'flirted')

        # Deleting field 'Player.equipped_armor'
        db.delete_column(u'players_player', 'equipped_armor_id')

        # Deleting field 'Player.equipped_weapon'
        db.delete_column(u'players_player', 'equipped_weapon_id')

        # Deleting field 'Player.gold'
        db.delete_column(u'players_player', 'gold')

        # Deleting field 'Player.bank'
        db.delete_column(u'players_player', 'bank')

        # Deleting field 'Player.gem'
        db.delete_column(u'players_player', 'gem')

        # Deleting field 'Player.last_alive_time'
        db.delete_column(u'players_player', 'last_alive_time')

        # Deleting field 'Player.last_dead_time'
        db.delete_column(u'players_player', 'last_dead_time')

        # Deleting field 'Player.days_played'
        db.delete_column(u'players_player', 'days_played')

        # Deleting field 'Player.death_knight_level'
        db.delete_column(u'players_player', 'death_knight_level')

        # Deleting field 'Player.death_knight_skill'
        db.delete_column(u'players_player', 'death_knight_skill')

        # Deleting field 'Player.mystical_level'
        db.delete_column(u'players_player', 'mystical_level')

        # Deleting field 'Player.mystical_skill'
        db.delete_column(u'players_player', 'mystical_skill')

        # Deleting field 'Player.theif_level'
        db.delete_column(u'players_player', 'theif_level')

        # Deleting field 'Player.theif_skill'
        db.delete_column(u'players_player', 'theif_skill')


        # Changing field 'Player.created_at'
        db.alter_column(u'players_player', 'created_at', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'players.armor': {
            'Meta': {'object_name': 'Armor'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.IntegerField', [], {})
        },
        u'players.monster': {
            'Meta': {'object_name': 'Monster'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'death': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'experience': ('django.db.models.fields.IntegerField', [], {}),
            'gold': ('django.db.models.fields.IntegerField', [], {}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'strength': ('django.db.models.fields.IntegerField', [], {}),
            'weapon': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['players.Weapon']"})
        },
        u'players.player': {
            'Meta': {'object_name': 'Player'},
            'bank': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'charm': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'days_played': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'dead': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'death_knight_level': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'death_knight_skill': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'done_special': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '255', 'db_index': 'True'}),
            'equipped_armor': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['players.Armor']", 'null': 'True'}),
            'equipped_weapon': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['players.Weapon']", 'null': 'True'}),
            'experience': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'fights_left': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'flirted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'gem': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gold': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'hit_points': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'hit_points_max': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'human_fights_left': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inn': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'kids': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'king': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'last_alive_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'auto_now_add': 'True', 'null': 'True', 'blank': 'True'}),
            'last_dead_time': ('django.db.models.fields.DateTimeField', [], {'default': 'None', 'null': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lays': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'level': ('django.db.models.fields.SmallIntegerField', [], {'default': '1'}),
            'married': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['players.Player']", 'null': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'mystical_level': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'mystical_skill': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'player_kills': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'seen_bard': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seen_dragon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seen_master': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'seen_violet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'strength': ('django.db.models.fields.IntegerField', [], {'default': '10'}),
            'theif_level': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'theif_skill': ('django.db.models.fields.SmallIntegerField', [], {'default': '0'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'weird_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'players.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'strength': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['players']