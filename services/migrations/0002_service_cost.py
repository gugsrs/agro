# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-01 03:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='cost',
            field=models.FloatField(default=0),
        ),
    ]