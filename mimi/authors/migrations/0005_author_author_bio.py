# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20150621_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='author_bio',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
