# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 05:24
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('title_image', models.URLField(default='http://i2.bvimg.com/620816/a0cc009306821447.jpg', null=True)),
                ('data_time', models.DateTimeField(auto_now_add=True)),
                ('content', ckeditor.fields.RichTextField(blank=True, verbose_name='内容')),
            ],
            options={
                'ordering': ['-data_time'],
            },
        ),
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.ArticleType'),
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Category'),
        ),
    ]