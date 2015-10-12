from django.db import models
from django.utils.translation import ugettext_lazy as _


class Album(models.Model):
    title = models.CharField(
        _('title'),
        max_length=150
      )
    artist = models.CharField(
      _('artist'),
        max_length=150
      )
    date_published = models.DateField(
        _('date published')
      )
    comments = models.TextField(
        _('detailed description'),
        null=True,
        blank=True
    )
    reference_code = models.CharField(
        _('reference code'),
        max_length=60,
        null=True,
        blank=True
      )
    picture = models.URLField(
        _('picture'),
        max_length=500,
        null=True,
        blank=True
      )
    genuine = models.BooleanField(
        _('genuine'),
        default=True
    )
    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"

    def __str__(self):
        return self.artist + ' - ' + self.title