# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-11 13:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0050_rename_last_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oaisource',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(1970, 1, 1, 0, 0)),
        ),
    ]
