# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 03:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0006_auto_20160125_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='district',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
