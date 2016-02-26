from django.db import models
from django.contrib.auth.models import User
from commons.models import TimeAuditModel

from taggit.managers import TaggableManager


class LinkManager(models.Manager):
    pass


class Bookmark(TimeAuditModel):
    link = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    user = models.ForeignKey(User)

    tags = TaggableManager(blank=True)

    def __unicode__(self):
        return self.title

    class Meta:
        unique_together = (('link', 'user'),)


class Favorite(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    user = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return "%s favorited %s" % (self.link, self.user)
