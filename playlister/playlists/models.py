from django.db import models
from datetime import datetime
from songs.models import Song

import pytz
import requests

thedate = pytz.utc


# Create your models here.

class Playlist(models.Model):

    playlistid = models.IntegerField(primary_key=True)
    name = models.CharField(default='The name of the playlist',
                            max_length=200)
    songs = models.ManyToManyField(Song)
    creator = models.CharField(default='The creator of the playlist',
                               max_length=200)
    cover_url = models.URLField()
    date = models.DateTimeField(auto_now=True, blank=True)
    description = models.CharField(default='A description of the playlist',
                                   max_length=200)
    featured_artists = models.CharField(default='A, list, of, the artists, formatted, like, this',
                                    max_length=200)
    song_count = models.IntegerField()

    songza_url = models.URLField()
    spotify_url = models.URLField()


    def get_similar(self):
        """
        Returns a list of playlists similar to self, this method uses the
        Songza api to retrieve the similar playlists

        http://songza.com/api/1/station/1392709/similar

        this returns a list of playlist objects in json similar to playlist with
        stationid=1392709

        """

        similar_url = 'http://songza.com/api/1/station/%s/similar'
        REQUEST_KWARGS = {'headers':HEADER, 'timeout':10.0, 'allow_redirects':False}

        similar = requests.get(similar_url%str(self.playlistid), **REQUEST_KWARGS)
        if similar.status_code != 200:
            return None
        else:
            similar = res.json()

        similar_ids = [station['id'] for station in similar]
        similar = Playlists.objects.filter(pk__in=similar_ids)

        return similar


    def __unicode__(self):
        return "Name: %s\n \
                Count: %s\n \
                Creator: %s\n \
                Added: %s\n \
                Pk: %s\n" % (self.name, self.song_count, self.creator, self.date,
                        self.playlistid)


class Group(models.Model):

    groupid = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, default='The name of the group')
    stations = models.ManyToManyField(Playlist)
    keywords = models.CharField(max_length=200, default='Some, key, words')
    date = models.DateTimeField(auto_now=True, blank=True)


class Category(models.Model):

    categoryid = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=200, default='The name of the category')
    groups = models.ManyToManyField(Group)
    date = models.DateTimeField(auto_now=True, blank=True)













