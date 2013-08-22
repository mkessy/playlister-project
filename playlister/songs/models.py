from django.db import models
from datetime import datetime, timedelta
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
    slug = models.SlugField(max_length=200)
    duration = models.IntegerField()
    genre = models.CharField(default='Song genre',
                             max_length=200)

    class Meta:
        ordering = ["title"]


    def __unicode__(self):
        return "Title: %s" % self.title

    def formatted_duration(self):
        return str(timedelta(seconds=self.duration))



