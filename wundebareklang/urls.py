from django.conf.urls import patterns, include, url
from django.contrib import admin
from wundebareklang import settings

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wundebareklang.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # Albums
    url(r'^my-albums/$','album.views.list_my_albums', name='my-albums'),
    url(r'^local-search/$','album.views.local_search', name='local-search'),
    url(r'^album/(?P<album_id>\d+)$', 'album.views.show_album', name='show-album'),
    
    url(r'^search/$', 'album.views.search_lastfm', name='search-lastfm'),
    
    url(r'^albums/add/$', 'album.views.add_collection_albums', name='add_albums'),
    url(r'^albums/add/(?P<album_mbid>\S+)$', 'album.views.add_album', name='add-album'),
    url(r'^add-album/$', 'album.views.add_album_manual', name='add-album-manual'),

    # Index
    url(r'^$', 'album.views.index', name='index'),

    )+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
