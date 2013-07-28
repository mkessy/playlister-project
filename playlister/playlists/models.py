from django.db import models
from datetime import datetime
from songs.models import Song
import pytz

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
    song_count = models.IntegerField()
    songza_url = models.URLField()
    spotify_url = models.URLField()

#   will implement later
#   categories = models.ManyToManyField(categories.Category)

    def __unicode__(self):
        return "Name: %s\n \
                Count: %s\n \
                Creator: %s\n \
                Added: %s\n \
                Pk: %s\n" % (self.name, self.song_count, self.creator, self.date,
                        self.playlistid)
