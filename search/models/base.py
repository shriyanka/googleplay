"""
Base model that can be inherited by other Models
"""

from django.db import models

class Base(models.Model):
    createdOn = models.DateTimeField(auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        app_label = 'search' 
