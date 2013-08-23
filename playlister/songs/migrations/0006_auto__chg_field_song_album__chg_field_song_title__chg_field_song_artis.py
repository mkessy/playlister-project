# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Song.album'
        db.alter_column(u'songs_song', 'album', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Song.title'
        db.alter_column(u'songs_song', 'title', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Song.artist'
        db.alter_column(u'songs_song', 'artist', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Song.genre'
        db.alter_column(u'songs_song', 'genre', self.gf('django.db.models.fields.CharField')(max_length=500))

        # Changing field 'Song.slug'
        db.alter_column(u'songs_song', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=500))

    def backwards(self, orm):

        # Changing field 'Song.album'
        db.alter_column(u'songs_song', 'album', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Song.title'
        db.alter_column(u'songs_song', 'title', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Song.artist'
        db.alter_column(u'songs_song', 'artist', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Song.genre'
        db.alter_column(u'songs_song', 'genre', self.gf('django.db.models.fields.CharField')(max_length=200))

        # Changing field 'Song.slug'
        db.alter_column(u'songs_song', 'slug', self.gf('django.db.models.fields.SlugField')(max_length=200))

    models = {
        u'songs.song': {
            'Meta': {'ordering': "['title']", 'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'default': "'Album name'", 'max_length': '500'}),
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Artist name'", 'max_length': '500'}),
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "'Song genre'", 'max_length': '500'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '500'}),
            'songid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Song title'", 'max_length': '500'})
        }
    }

    complete_apps = ['songs']