# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=255, db_index=True, verbose_name='name')),
                ('url', models.URLField(max_length=255, blank=True, verbose_name='url')),
                ('screenshot', models.URLField(max_length=255, blank=True, verbose_name='screen')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('duration', models.DurationField(blank=True, verbose_name='duration', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(unique=True, max_length=50, db_index=True, verbose_name='name')),
                ('icon', models.URLField(max_length=255, blank=True, verbose_name='icon')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', to='portfolio.Technology', blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(related_name='projects', to='portfolio.Technology', verbose_name='technologies'),
        ),
    ]
