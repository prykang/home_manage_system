# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiction', '0005_auto_20181114_1610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fictioninfo',
            name='author',
        ),
    ]