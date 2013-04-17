# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Terrain'
        db.create_table(u'world_terrain', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('fg_color', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('bg_color', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('character', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('turns', self.gf('django.db.models.fields.IntegerField')(default=1)),
            ('passable', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'world', ['Terrain'])

        # Adding model 'WorldMap'
        db.create_table(u'world_worldmap', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('level_min', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'world', ['WorldMap'])

        # Adding model 'MapSquare'
        db.create_table(u'world_mapsquare', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, auto_now_add=True, blank=True)),
            ('world_map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.MapSquare'])),
            ('x', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('y', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('terrain', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['world.Terrain'])),
            ('battle_odds', self.gf('django.db.models.fields.IntegerField')()),
            ('safe', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'world', ['MapSquare'])

        # Adding unique constraint on 'MapSquare', fields ['world_map', 'x', 'y']
        db.create_unique(u'world_mapsquare', ['world_map_id', 'x', 'y'])


    def backwards(self, orm):
        # Removing unique constraint on 'MapSquare', fields ['world_map', 'x', 'y']
        db.delete_unique(u'world_mapsquare', ['world_map_id', 'x', 'y'])

        # Deleting model 'Terrain'
        db.delete_table(u'world_terrain')

        # Deleting model 'WorldMap'
        db.delete_table(u'world_worldmap')

        # Deleting model 'MapSquare'
        db.delete_table(u'world_mapsquare')


    models = {
        u'world.mapsquare': {
            'Meta': {'unique_together': "(('world_map', 'x', 'y'),)", 'object_name': 'MapSquare'},
            'battle_odds': ('django.db.models.fields.IntegerField', [], {}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'auto_now_add': 'True', 'blank': 'True'}),
            'safe': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'terrain': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['world.Terrain']"}),
            'world_map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['world.MapSquare']"}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['world']