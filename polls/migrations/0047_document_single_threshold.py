# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 00:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0046_auto_20160715_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='single_threshold',
            field=models.BooleanField(default=False),
        ),
    ]