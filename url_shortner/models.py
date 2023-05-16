""" URL Shortner model for storing urls."""
from django.db import models

class URLBase(models.Model):

    id = models.BigIntegerField(primary_key=True,auto_created=True)
    url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=30)

    def __str__(self):
        return id
    