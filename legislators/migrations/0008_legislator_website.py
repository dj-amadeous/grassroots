# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0007_auto_20160125_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='legislator',
            name='website',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
    ]
