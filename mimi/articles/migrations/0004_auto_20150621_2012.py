# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150621_1958'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
                'db_table': 'article_tag',
            },
        ),
        migrations.AlterField(
            model_name='article',
            name='public_uuid',
            field=models.UUIDField(primary_key=True, default=uuid.uuid4, serialize=False, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterModelTable(
            name='article',
            table='article',
        ),
    ]
