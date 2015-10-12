# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='title', max_length=150)),
                ('artist', models.CharField(verbose_name='artist', max_length=150)),
                ('date_published', models.DateField(verbose_name='date published')),
                ('comments', models.TextField(verbose_name='detailed description', null=True, blank=True)),
                ('reference_code', models.CharField(verbose_name='reference code', null=True, max_length=60, blank=True)),
                ('picture', models.URLField(verbose_name='picture', null=True, max_length=500, blank=True)),
                ('genuine', models.BooleanField(verbose_name='genuine', default=True)),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', null=True, max_length=50, blank=True)),
                ('album', models.ForeignKey(verbose_name='album', to='album.Album', related_name='genre_albums', related_query_name='genre_album')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(verbose_name='title', max_length=500)),
                ('duration', models.CharField(verbose_name='duration', max_length=10)),
                ('rank', models.PositiveIntegerField(verbose_name='rank', null=True, blank=True)),
                ('album', models.ForeignKey(verbose_name='album', to='album.Album', related_name='song_albums', related_query_name='song_album')),
            ],
            options={
                'verbose_name': 'Song',
                'verbose_name_plural': 'Songs',
            },
            bases=(models.Model,),
        ),
    ]
