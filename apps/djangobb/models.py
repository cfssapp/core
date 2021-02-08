from django.db import models
from django.conf import settings

from django.utils import timezone
from datetime import datetime


class Topic(models.Model):
    forum = models.CharField(max_length=100, default="not set")
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    views = models.IntegerField(blank=True, default=0)
    post_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.updated is None:
            self.updated = timezone.now()
        super(Topic, self).save(*args, **kwargs)