# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_auto_20161216_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
