# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Player.world_map'
        db.add_column(u'players_player', 'world_map',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['world.WorldMap']),
                      keep_default=False)

        # Adding field 'Player.map_square'
        db.add_column(u'players_player', 'map_square',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['world.MapSquare']),
                      keep_default=False)

        # Adding field 'Player.here_since'
        db.add_column(u'players_player', 'here_since',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 4, 12, 0, 0), auto_now_add=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Player.world_map'
        db.delete_column(u'players_player', 'world_map_id')

        # Deleting field 'Player.map_square'
        db.delete_column(u'players_player', 'map_square_id')

        # Deleting field 'Player.here_since'
        db.delete_column(u'players_player', 'here_since')


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
            'here_since': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 4, 12, 0, 0)', 'auto_now_add': 'True', 'blank': 'True'}),
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
            'map_square': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['world.MapSquare']"}),
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
            'weird_event': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'world_map': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['world.WorldMap']"})
        },
        u'players.weapon': {
            'Meta': {'object_name': 'Weapon'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'price': ('django.db.models.fields.IntegerField', [], {}),
            'strength': ('django.db.models.fields.IntegerField', [], {})
        },
        u'world.mapsquare': {
            'Meta': {'ordering': "('world_map', 'x', 'y')", 'unique_together': "(('world_map', 'x', 'y'),)", 'object_name': 'MapSquare'},
            'battle_odds': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'terrain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['world.Terrain']"}),
            'world_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['world.WorldMap']"}),
            'x': ('django.db.models.fields.SmallIntegerField', [], {}),
            'y': ('django.db.models.fields.SmallIntegerField', [], {})
        },
        u'world.terrain': {
            'Meta': {'object_name': 'Terrain'},
            'bg_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'character': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fg_color': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'passable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'turns': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        u'world.worldmap': {
            'Meta': {'ordering': "['level_min']", 'object_name': 'WorldMap'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_min': ('django.db.models.fields.SmallIntegerField', [], {}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'start': ('django.db.models.fields.related.ForeignKey', [], {'default': '1', 'to': u"orm['world.MapSquare']"}),
            'x_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            'y_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['players']