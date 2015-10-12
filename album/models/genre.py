from django.db import models
from django.utils.translation import ugettext_lazy as _


class Genre(models.Model):
    name = models.CharField(
        _('name'),
        max_length=50,
        null=True,
        blank=True
      )
    album = models.ForeignKey(
        'Album',
        related_name='genre_albums',
        related_query_name='genre_album',
        verbose_name=_('album')
      )
    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.album.title + '-' + self.name
    
      
    