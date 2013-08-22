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
            ('featured_artists', self.gf('django.db.models.fields.CharField')(default='A, list, of, the artists, formatted, like, this', max_length=200)),
            ('song_count', self.gf('django.db.models.fields.IntegerField')()),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
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

        # Adding model 'Group'
        db.create_table(u'playlists_group', (
            ('groupid', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='The name of the group', max_length=200)),
            ('keywords', self.gf('django.db.models.fields.CharField')(default='Some, key, words', max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'playlists', ['Group'])

        # Adding M2M table for field stations on 'Group'
        db.create_table(u'playlists_group_stations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm[u'playlists.group'], null=False)),
            ('playlist', models.ForeignKey(orm[u'playlists.playlist'], null=False))
        ))
        db.create_unique(u'playlists_group_stations', ['group_id', 'playlist_id'])

        # Adding model 'Category'
        db.create_table(u'playlists_category', (
            ('categoryid', self.gf('django.db.models.fields.CharField')(max_length=200, primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(default='The name of the category', max_length=200)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=200)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'playlists', ['Category'])

        # Adding M2M table for field groups on 'Category'
        db.create_table(u'playlists_category_groups', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'playlists.category'], null=False)),
            ('group', models.ForeignKey(orm[u'playlists.group'], null=False))
        ))
        db.create_unique(u'playlists_category_groups', ['category_id', 'group_id'])


    def backwards(self, orm):
        # Deleting model 'Playlist'
        db.delete_table(u'playlists_playlist')

        # Removing M2M table for field songs on 'Playlist'
        db.delete_table('playlists_playlist_songs')

        # Deleting model 'Group'
        db.delete_table(u'playlists_group')

        # Removing M2M table for field stations on 'Group'
        db.delete_table('playlists_group_stations')

        # Deleting model 'Category'
        db.delete_table(u'playlists_category')

        # Removing M2M table for field groups on 'Category'
        db.delete_table('playlists_category_groups')


    models = {
        u'playlists.category': {
            'Meta': {'ordering': "['name']", 'object_name': 'Category'},
            'categoryid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Group']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the category'", 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'})
        },
        u'playlists.group': {
            'Meta': {'ordering': "['name']", 'object_name': 'Group'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'groupid': ('django.db.models.fields.CharField', [], {'max_length': '200', 'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.CharField', [], {'default': "'Some, key, words'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the group'", 'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'stations': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['playlists.Playlist']", 'symmetrical': 'False'})
        },
        u'playlists.playlist': {
            'Meta': {'ordering': "['name']", 'object_name': 'Playlist'},
            'cover_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'creator': ('django.db.models.fields.CharField', [], {'default': "'The creator of the playlist'", 'max_length': '200'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'default': "'A description of the playlist'", 'max_length': '200'}),
            'featured_artists': ('django.db.models.fields.CharField', [], {'default': "'A, list, of, the artists, formatted, like, this'", 'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'default': "'The name of the playlist'", 'max_length': '200'}),
            'playlistid': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '200'}),
            'song_count': ('django.db.models.fields.IntegerField', [], {}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['songs.Song']", 'symmetrical': 'False'}),
            'songza_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'spotify_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
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

    complete_apps = ['playlists']