# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_auto_20150621_2014'),
        ('articles', '0005_auto_20150621_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(blank=True, to='authors.Author', null=True),
        ),
    ]
