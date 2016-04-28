# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('app_id', models.CharField(max_length=64, null=True, blank=True)),
                ('app_name', models.CharField(max_length=128, null=True, blank=True)),
                ('developer_name', models.CharField(max_length=128, null=True, blank=True)),
                ('developer_email', models.EmailField(max_length=128)),
                ('icon_url', models.URLField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchResultApp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('app', models.ForeignKey(to='search.Apps')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SearchTerm',
            fields=[
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('updatedOn', models.DateTimeField(auto_now=True)),
                ('term', models.CharField(max_length=128, serialize=False, primary_key=True)),
                ('apps', models.ManyToManyField(related_name='apps', through='search.SearchResultApp', to='search.Apps')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='searchresultapp',
            name='term',
            field=models.ForeignKey(to='search.SearchTerm'),
        ),
    ]
