# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-20 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20180320_0113'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
