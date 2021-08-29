from django.db import models
from django.conf import settings

from django.utils import timezone
from datetime import datetime


class Comment(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    cert_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content

class Certificate(models.Model):
    certificate_id = models.CharField(max_length=100, default="not set")
    instrument = models.CharField(max_length=100, default="not set")
    customer = models.CharField(max_length=100, default="not set")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.certificate_id
