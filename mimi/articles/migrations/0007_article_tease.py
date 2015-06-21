# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='tease',
            field=models.CharField(max_length=1000, null=True, blank=True),
        ),
    ]
