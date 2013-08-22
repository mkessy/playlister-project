# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Song'
        db.create_table(u'songs_song', (
            ('songid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('album', self.gf('django.db.models.fields.CharField')(default='Album name', max_length=200)),
            ('title', self.gf('django.db.models.fields.CharField')(default='Song title', max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('artist', self.gf('django.db.models.fields.CharField')(default='Artist name', max_length=200)),
            ('cover_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('duration', self.gf('django.db.models.fields.IntegerField')()),
            ('genre', self.gf('django.db.models.fields.CharField')(default='Song genre', max_length=200)),
        ))
        db.send_create_signal(u'songs', ['Song'])


    def backwards(self, orm):
        # Deleting model 'Song'
        db.delete_table(u'songs_song')


    models = {
        u'songs.song': {
            'Meta': {'ordering': "['title']", 'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'default': "'Album name'", 'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Artist name'", 'max_length': '200'}),
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "'Song genre'", 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'songid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Song title'", 'max_length': '200'})
        }
    }

    complete_apps = ['songs']