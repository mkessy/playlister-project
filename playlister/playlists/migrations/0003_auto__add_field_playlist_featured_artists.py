# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Playlist.featured_artists'
        db.add_column(u'playlists_playlist', 'featured_artists',
                      self.gf('django.db.models.fields.CharField')(default='A, list, of, the artists, formatted, like, this', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Playlist.featured_artists'
        db.delete_column(u'playlists_playlist', 'featured_artists')


    models = {
        u'playlists.category': {
            'Meta': {'object_name': 'Category'},
            'categoryid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Group']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the category'", 'max_length': '200'})
        },
        u'playlists.group': {
            'Meta': {'object_name': 'Group'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "'Some, key, words'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the group'", 'max_length': '200'}),
            'stations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Playlist']", 'symmetrical': 'False'})
        },
        u'playlists.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'creator': ('django.db.models.fields.CharField', [], {'default': "'The creator of the playlist'", 'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'A description of the playlist'", 'max_length': '200'}),
            'featured_artists': ('django.db.models.fields.CharField', [], {'default': "'A, list, of, the artists, formatted, like, this'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the playlist'", 'max_length': '200'}),
            'playlistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'song_count': ('django.db.models.fields.IntegerField', [], {}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['songs.Song']", 'symmetrical': 'False'}),
            'songza_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'spotify_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'songs.song': {
            'Meta': {'object_name': 'Song'},
            'album': ('django.db.models.fields.CharField', [], {'default': "'Album name'", 'max_length': '200'}),
            'artist': ('django.db.models.fields.CharField', [], {'default': "'Artist name'", 'max_length': '200'}),
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "'Song genre'", 'max_length': '200'}),
            'songid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Song title'", 'max_length': '200'})
        }
    }

    complete_apps = ['playlists']