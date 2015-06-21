import uuid

from django.db import models

class Article(models.Model):
    """An article for publication on the Mimi web site.

    """
    public_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)

    headline = models.CharField(max_length=500)
    subheadline = models.CharField(max_length=500, null=True, blank=True)
    author = models.ForeignKey('authors.Author', null=True, blank=True)

    content = models.TextField()
    tease = models.CharField(max_length=1000, null=True, blank=True)

    slug = models.SlugField(unique=True)
    published = models.BooleanField(default=False)
    publication_dt = models.DateTimeField(auto_now=True, editable=True)

    @property
    def article_tease(self):
        if self.tease:
            return self.tease

        ## TODO: Calculate the tease by either looking for a
        ##       tease marker, using the first paragraph, or
        ##       parsing out up to, say, 100 words.
        return self.content


    def __unicode__(self):
        return '%s (UUID: %s)' % (self.headline, self.public_uuid)

    class Meta:
        db_table = 'article'


class ArticleTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'article_tag'

class ArticleArticleTag(models.Model):
    article = models.ForeignKey('Article', related_name='tags')
    tag = models.ForeignKey('ArticleTag', related_name='articles')

    def __unicode__(self):
        return '%s / %s' (self.article, self.tag)

    class Meta:
        db_table = 'article_article_tag'
        unique_together = ('article', 'tag')
