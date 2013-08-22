from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from playlists.views import home
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^$', home, name="home" ),
        url(r'^items/', include('playlists.urls')),

    # Examples:
    # url(r'^$', 'playlister.views.home', name='home'),
    # url(r'^playlister/', include('playlister.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
