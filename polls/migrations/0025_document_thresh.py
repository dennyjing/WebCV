# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 09:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0024_auto_20160712_1712'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='thresh',
            field=models.IntegerField(default=157, max_length=16),
        ),
    ]
