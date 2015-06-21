# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150621_2012'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleArticleTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(related_name='tags', to='articles.Article')),
                ('tag', models.ForeignKey(related_name='articles', to='articles.ArticleTag')),
            ],
            options={
                'db_table': 'article_article_tag',
            },
        ),
        migrations.AlterUniqueTogether(
            name='articlearticletag',
            unique_together=set([('article', 'tag')]),
        ),
    ]
