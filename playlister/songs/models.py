from django.db import models
from datetime import datetime
import pytz

thedate = pytz.utc

# Create your models here.

class Song(models.Model):

    songid = models.IntegerField(primary_key=True)
    album = models.CharField(default='Album name',
                             max_length=200)
    title  = models.CharField(default='Song title',
                              max_length=200)

    date = models.DateTimeField(default=datetime.now, blank=True)
    artist = models.CharField(default='Artist name',
                              max_length=200)
    cover_url = models.URLField()
    duration = models.IntegerField()
    genre = models.CharField(default='Song genre',
                             max_length=200)
    # possibly add a relationship with Category

    def __unicode__(self):
        return "Title: %s\n \
                Artist: %s\n \
                Album: %s\n \
                Genre: %s\n \
                Runtime: %s\n \
                Added: %s\n \
                Pk: %s\n" % (self.title, self.artist, self.album, self.genre, self.duration,
                        self.date, self.songid)
