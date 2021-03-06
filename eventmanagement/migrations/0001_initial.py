# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-10 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(default='')),
                ('location', models.CharField(max_length=100)),
                ('startdate', models.DateTimeField(blank=True, null=True)),
                ('enddate', models.DateTimeField(blank=True, null=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='files/%Y/%m/%d')),
                ('category', models.CharField(max_length=100)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'event_management_details',
            },
        ),
    ]
