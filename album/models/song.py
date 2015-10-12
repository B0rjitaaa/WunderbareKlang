from django.db import models
from django.utils.translation import ugettext_lazy as _


class Song(models.Model):
    title = models.CharField(
        _('title'),
        max_length=500
      )
    duration = models.CharField(
        _('duration'),
        max_length=10
      )
    rank = models.PositiveIntegerField(
        _('rank'),
        null=True,
        blank=True
      )
    album = models.ForeignKey(
        'Album',
        related_name='song_albums',
        related_query_name='song_album',
        verbose_name=_('album')
      )
    class Meta:
        verbose_name = "Song"
        verbose_name_plural = "Songs"

    def __str__(self):
      return self.title + ':' + self.duration