import datetime

from django import forms
from django.forms.models import inlineformset_factory
from django.forms.utils import ErrorList

from album.models import *


class TextError(ErrorList):
    def __str__(self):
        return self.as_span()
    def as_span(self):
        if not self:
            return ''
        return self[0]


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album


class SongForm(forms.ModelForm):
    class Meta:
        model = Song