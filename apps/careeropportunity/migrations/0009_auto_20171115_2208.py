# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-15 21:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careeropportunity', '0008_auto_20171108_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careeropportunity',
            name='deadline',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='frist'),
        ),
        migrations.AlterField(
            model_name='careeropportunity',
            name='end',
            field=models.DateTimeField(verbose_name='aktiv til'),
        ),
        migrations.AlterField(
            model_name='careeropportunity',
            name='start',
            field=models.DateTimeField(verbose_name='aktiv fra'),
        ),
    ]