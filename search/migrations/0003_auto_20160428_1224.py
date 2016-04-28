# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_auto_20160428_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchterm',
            name='count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='searchterm',
            name='apps',
            field=models.ManyToManyField(related_name='apps', through='search.SearchResultApp', to='search.Apps', blank=True),
        ),
    ]
