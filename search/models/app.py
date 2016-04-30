from .base import Base
from django.db import models

# You can do a better DB design for this specific problem.
# Will share the design after I create one.

class Apps(Base):
    app_id = models.CharField(max_length=64, primary_key=True)
    app_name = models.CharField(max_length=256, null=True, blank=True)
    developer_name = models.CharField(max_length=128, null=True, blank=True)
    developer_email = models.EmailField(max_length=128)
    published = models.CharField(max_length=32, null=True, blank=True)
    icon_url = models.URLField(max_length=256)
    price = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        default="Free")

    def __str__(self):
        return self.app_name


class SearchTerm(Base):
    term = models.CharField(max_length=128, primary_key=True)
    apps = models.ManyToManyField(
        'Apps',
        related_name='apps',
        through='SearchResultApp',
        blank=True)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.term


class SearchResultApp(Base):
    app = models.ForeignKey('Apps')
    term = models.ForeignKey('SearchTerm')
