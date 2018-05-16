# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-16 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20180516_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='authors', to='books.Book'),
        ),
    ]