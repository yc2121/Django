# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-29 19:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=datetime.datetime(2018, 5, 29, 19, 28, 17, 830000, tzinfo=utc), max_length=30),
            preserve_default=False,
        ),
    ]
