from django.conf import settings
from django.db import models
from django_extensions.db.fields import AutoSlugField

class Author(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL, unique=True)
    display_name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, populate_from=('display_name',))
    photo = models.ImageField(null=True, blank=True)
    author_bio = models.CharField(max_length=1000, null=True, blank=True)

    def __unicode__(self):
        return '%s (%s)' % (self.display_name, self.slug)

    class Meta:
        db_table = 'author'
