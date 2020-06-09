# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-08 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('tel_num', models.PositiveIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('balance', models.FloatField(default=0)),
            ],
        ),
    ]