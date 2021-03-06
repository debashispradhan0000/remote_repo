# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-11-27 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('author', models.CharField(max_length=256)),
                ('pages', models.PositiveIntegerField()),
                ('price', models.FloatField()),
            ],
        ),
    ]
