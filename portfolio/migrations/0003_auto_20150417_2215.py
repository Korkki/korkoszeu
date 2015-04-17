# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20150417_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_en',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='project',
            name='description_pl',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='project',
            name='name_en',
            field=models.CharField(db_index=True, max_length=255, unique=True, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='project',
            name='name_pl',
            field=models.CharField(db_index=True, max_length=255, unique=True, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='technology',
            name='name_en',
            field=models.CharField(db_index=True, max_length=50, unique=True, null=True, verbose_name='name'),
        ),
        migrations.AddField(
            model_name='technology',
            name='name_pl',
            field=models.CharField(db_index=True, max_length=50, unique=True, null=True, verbose_name='name'),
        ),
    ]
