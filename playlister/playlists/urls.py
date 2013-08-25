from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from playlists.views import playlist, category, group
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

       url(r'^playlist/(?P<playlistid>\d+)/$', playlist, name="playlist"),
       url(r'^playlist/(?P<playlistid>\d+)/(?P<slug>[-\w]+)/$', playlist, name="playlist_slug"),

       #       url(r'^playlist/(?P<slug>[-\w]+)/$', playlist, name="playlist"),

       url(r'^category/(?P<categoryid>[-\w]+)/$', category, name="category"),
       url(r'^group/(?P<groupid>[-\w]+)/$', group, name="group"),


       )

