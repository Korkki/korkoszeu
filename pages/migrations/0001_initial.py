# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('title_pl', models.CharField(max_length=50, null=True, verbose_name='title')),
                ('title_en', models.CharField(max_length=50, null=True, verbose_name='title')),
                ('slug', models.SlugField(max_length=55, verbose_name='slug', unique=True)),
                ('slug_pl', models.SlugField(max_length=55, null=True, verbose_name='slug', unique=True)),
                ('slug_en', models.SlugField(max_length=55, null=True, verbose_name='slug', unique=True)),
                ('description', models.CharField(max_length=200, blank=True, verbose_name='description')),
                ('description_pl', models.CharField(max_length=200, blank=True, null=True, verbose_name='description')),
                ('description_en', models.CharField(max_length=200, blank=True, null=True, verbose_name='description')),
                ('content', models.TextField(verbose_name='content')),
                ('content_pl', models.TextField(null=True, verbose_name='content')),
                ('content_en', models.TextField(null=True, verbose_name='content')),
                ('publish', models.BooleanField(default=False, verbose_name='published')),
                ('template_name', models.CharField(max_length=70, blank=True, verbose_name='template name')),
                ('last_mod', models.DateTimeField(verbose_name='last modification', auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='creation date')),
                ('sites', models.ManyToManyField(to='sites.Site', related_name='pages', verbose_name='sites')),
            ],
            options={
                'get_latest_by': 'creation_date',
                'ordering': ['-creation_date'],
                'verbose_name_plural': 'pages',
                'verbose_name': 'page',
            },
        ),
    ]
