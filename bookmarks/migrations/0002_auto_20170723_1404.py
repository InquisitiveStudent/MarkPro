# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsboard',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
