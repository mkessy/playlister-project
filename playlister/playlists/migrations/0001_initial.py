# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Playlist'
        db.create_table(u'playlists_playlist', (
            ('playlistid', self.gf('django.db.models.fields.IntegerField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='The name of the playlist', max_length=200)),
            ('creator', self.gf('django.db.models.fields.CharField')(default='The creator of the playlist', max_length=200)),
            ('cover_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='A description of the playlist', max_length=200)),
            ('song_count', self.gf('django.db.models.fields.IntegerField')()),
            ('songza_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('spotify_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'playlists', ['Playlist'])

        # Adding M2M table for field songs on 'Playlist'
        db.create_table(u'playlists_playlist_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('playlist', models.ForeignKey(orm[u'playlists.playlist'], null=False)),
            ('song', models.ForeignKey(orm[u'songs.song'], null=False))
        ))
        db.create_unique(u'playlists_playlist_songs', ['playlist_id', 'song_id'])


    def backwards(self, orm):
        # Deleting model 'Playlist'
        db.delete_table(u'playlists_playlist')

        # Removing M2M table for field songs on 'Playlist'
        db.delete_table('playlists_playlist_songs')


    models = {
        u'playlists.playlist': {
            'Meta': {'object_name': 'Playlist'},
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'creator': ('django.db.models.fields.CharField', [], {'default': "'The creator of the playlist'", 'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'A description of the playlist'", 'max_length': '200'}),
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
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'duration': ('django.db.models.fields.IntegerField', [], {}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "'Song genre'", 'max_length': '200'}),
            'songid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Song title'", 'max_length': '200'})
        }
    }

    complete_apps = ['playlists']