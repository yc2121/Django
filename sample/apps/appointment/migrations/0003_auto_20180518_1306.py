# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-18 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0002_user_dob'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='thedate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='thetime',
            field=models.TimeField(),
        ),
    ]
