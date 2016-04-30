"""
Base model that can be inherited by other Models
"""

from django.db import models


# Nice - I loke this. Its alyways good to have a base model.
# I always have a basemodel :)

class Base(models.Model):
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        app_label = 'search'
