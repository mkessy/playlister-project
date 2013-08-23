from django.db import models
from datetime import datetime, timedelta
from songs.models import Song

import pytz
import requests

thedate = pytz.utc


# Create your models here.

class Playlist(models.Model):

    playlistid = models.IntegerField(primary_key=True)
    name = models.CharField(default='The name of the playlist',
                            max_length=500)
    songs = models.ManyToManyField(Song)
    creator = models.CharField(default='The creator of the playlist',
                               max_length=500)
    cover_url = models.URLField()
    date = models.DateTimeField(auto_now=True, blank=True)
    description = models.CharField(default='A description of the playlist',
                                   max_length=500)
    featured_artists = models.CharField(default='A, list, of, the artists, formatted, like, this',
                                    max_length=500)
    song_count = models.IntegerField()

    slug = models.SlugField(max_length=500)

    songza_url = models.URLField()
    spotify_url = models.URLField()

    class Meta:
        ordering = ["name"]


    def get_similar(self):
        """
        Returns a list of playlists similar to self, this method uses the
        Songza api to retrieve the similar playlists

        http://songza.com/api/1/station/1392709/similar

        this returns a list of playlist objects in json similar to playlist with
        stationid=1392709

        """

        similar_url = 'http://songza.com/api/1/station/%s/similar'

        HEADER = {"User-Agent":
                "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0)"}


        REQUEST_KWARGS = {'headers':HEADER, 'timeout':10.0, 'allow_redirects':False}

        similar = requests.get(similar_url%str(self.playlistid), **REQUEST_KWARGS)
        if similar.status_code != 200:
            return None
        else:
            similar = similar.json()

        similar_ids = [station['id'] for station in similar]
        similar = Playlist.objects.filter(pk__in=similar_ids)

        return similar



    def __unicode__(self):
        return "%s" % (self.name)

    def formatted_duration(self):
        total_duration = 0
        for song in self.songs.all():
            total_duration += song.duration
        return str(timedelta(seconds=total_duration))



class Group(models.Model):

    groupid = models.CharField(primary_key=True, max_length=500)
    name = models.CharField(max_length=500, default='The name of the group')
    stations = models.ManyToManyField(Playlist)
    keywords = models.CharField(max_length=500, default='Some, key, words')
    slug = models.SlugField(max_length=500)
    date = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering = ["name"]

    def __unicode__(self):
        return "%s" % (self.name)

    def chunk_4(self):
        from playlist_helpers import chunk_list
        return chunk_list(self.stations.all(), 4)

    def chunk_3(self):
        from playlist_helpers import chunk_list
        return chunk_list(self.stations.all(), 3)


    def __unicode__(self):
        return "%s" % (self.name)


class Category(models.Model):

    categoryid = models.CharField(primary_key=True, max_length=500)
    name = models.CharField(max_length=500, default='The name of the category')
    groups = models.ManyToManyField(Group)

    slug = models.SlugField(max_length=500)
    date = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        ordering=["name"]

    def __unicode__(self):
        return "%s" % (self.name)

    def chunk_10(self):
        from playlist_helpers import chunk_list
        return chunk_list(self.groups.all(), 10)

    def chunk_8(self):
        from playlist_helpers import chunk_list
        return chunk_list(self.groups.all(), 8)

    def chunk_12(self):
        from playlist_helpers import chunk_list
        return chunk_list(self.groups.all(), 12)




