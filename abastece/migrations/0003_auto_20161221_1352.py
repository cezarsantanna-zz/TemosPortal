# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abastece', '0002_auto_20161221_0034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='punch',
            name='coordX',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='punch',
            name='coordY',
            field=models.CharField(max_length=15, null=True),
        ),
    ]