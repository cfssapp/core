from django.db import models
from django.conf import settings

from django.utils import timezone
from datetime import datetime


class Certificate(models.Model):
    certificate_id = models.CharField(max_length=100, default="not set")
    instrument = models.CharField(max_length=100, default="not set")
    customer = models.CharField(max_length=100, default="not set")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.certificate_id
