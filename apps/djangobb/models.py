from django.db import models
from django.conf import settings

from django.utils import timezone
from datetime import datetime


class Post(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    topic_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content

class Topic(models.Model):
    forum = models.CharField(max_length=100, default="not set")
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    views = models.IntegerField(blank=True, default=0)
    post_count = models.IntegerField(blank=True, default=0)
    posts = models.ManyToManyField(Post, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.created is not None:
            self.updated = timezone.now()
        super(Topic, self).save(*args, **kwargs)