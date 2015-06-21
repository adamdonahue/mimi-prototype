# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_auto_20150621_1958'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='author',
            table='author',
        ),
    ]
