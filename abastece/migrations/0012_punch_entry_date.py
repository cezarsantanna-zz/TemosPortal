# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastece', '0011_auto_20161227_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='punch',
            name='entry_date',
            field=models.DateField(default='1970-01-01'),
        ),
    ]
