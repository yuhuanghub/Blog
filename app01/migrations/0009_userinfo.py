# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0008_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('pwd', models.IntegerField(max_length=20)),
            ],
        ),
    ]
