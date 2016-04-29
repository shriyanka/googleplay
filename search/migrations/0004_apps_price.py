# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_auto_20160428_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='price',
            field=models.CharField(default=b'Free', max_length=64, null=True, blank=True),
        ),
    ]
