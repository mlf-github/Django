# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-06-27 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=30)),
                ('upwd', models.CharField(max_length=30)),
                ('uemail', models.EmailField(max_length=254)),
                ('uage', models.IntegerField()),
            ],
        ),
    ]
