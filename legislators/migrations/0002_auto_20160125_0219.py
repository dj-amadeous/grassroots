# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-25 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legislators', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legislator',
            name='contact_form',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='crp_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='district',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='facebook_id',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='fax',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='govtrack_id',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='leadership_role',
            field=models.CharField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='middle_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='name_suffix',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='nickname',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='oc_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='ocd_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='office',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='party',
            field=models.CharField(blank=True, choices=[('R', 'Republican'), ('D', 'Democrat'), ('I', 'Independent'), ('G', 'Green')], max_length=1),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='phone',
            field=models.CharField(blank=True, max_length=14),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='thomas_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='title',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='legislator',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
