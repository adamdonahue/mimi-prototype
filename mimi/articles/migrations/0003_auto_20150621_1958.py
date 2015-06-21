# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='subheadline',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
    ]
