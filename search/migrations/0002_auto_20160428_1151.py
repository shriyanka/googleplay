# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchterm',
            name='apps',
            field=models.ManyToManyField(related_name='apps', null=True, through='search.SearchResultApp', to='search.Apps', blank=True),
        ),
    ]
