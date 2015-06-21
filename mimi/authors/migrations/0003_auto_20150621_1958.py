# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0002_author_display_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(editable=False, populate_from=(b'display_name',), blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='display_name',
            field=models.CharField(max_length=100),
        ),
    ]
