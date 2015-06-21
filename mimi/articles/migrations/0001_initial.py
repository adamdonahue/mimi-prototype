# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('public_uuid', models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True)),
                ('headline', models.CharField(max_length=500)),
                ('subheadline', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('published', models.BooleanField(default=False)),
                ('publication_dt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
