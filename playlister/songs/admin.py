#admin interface for model Song

from django.contrib import admin
from songs.models import Song

admin.site.register(Song)
