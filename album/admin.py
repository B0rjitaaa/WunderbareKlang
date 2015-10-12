from django.contrib import admin
from album.models import *

admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Genre)

