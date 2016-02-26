from django.db import models


class TimeAuditModel(models.Model):

    """ To track when the record was created and last modified """
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Created At",)
    modified_at = models.DateTimeField(
        auto_now=True, verbose_name="Last Modified At")

    class Meta:
        abstract = True
