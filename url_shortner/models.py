""" URL Shortner model for storing urls."""
from django.db import models

class URLBase(models.Model):

    url = models.URLField(max_length=255)
    short_url = models.URLField(max_length=30,unique=True)

    def __str__(self):
        return self.short_url
    

    class Meta:
        db_table = 'url_base'