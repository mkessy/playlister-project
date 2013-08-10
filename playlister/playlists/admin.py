#admin interface for model Playlist

from django.contrib import admin
from playlists.models import Playlist

admin.site.register(Playlist)
