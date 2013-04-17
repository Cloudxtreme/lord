# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'MapSquare.world_map'
        db.alter_column(u'world_mapsquare', 'world_map_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.WorldMap']))

    def backwards(self, orm):

        # Changing field 'MapSquare.world_map'
        db.alter_column(u'world_mapsquare', 'world_map_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.MapSquare']))

    models = {
        u'world.mapsquare': {
            'Meta': {'unique_together': "(('world_map', 'x', 'y'),)", 'object_name': 'MapSquare'},
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
            'Meta': {'object_name': 'WorldMap'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level_min': ('django.db.models.fields.SmallIntegerField', [], {}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'x_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'}),
            'y_size': ('django.db.models.fields.SmallIntegerField', [], {'default': '10'})
        }
    }

    complete_apps = ['world']