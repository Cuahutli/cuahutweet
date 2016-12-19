# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-16 22:23
from __future__ import unicode_literals

from django.db import migrations, models
import tweets.models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_tweet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=140, validators=[tweets.models.validate_content]),
        ),
    ]