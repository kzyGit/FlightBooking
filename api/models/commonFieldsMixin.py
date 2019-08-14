from django.db import models


class CommonFieldsMixin(models.Model):
    """ common fields model """
    dateAdded = models.DateTimeField(auto_now_add=True)
    dateModified = models.DateTimeField(auto_now=True)

    class Meta:
        """ Metadata options """
        abstract = True
