# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 14:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbtmApp', '0002_temperaturesensor_localsensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressionsensor',
            name='localSensor',
            field=models.IntegerField(db_index=True, db_tablespace=b'indexes', default=0),
        ),
    ]
