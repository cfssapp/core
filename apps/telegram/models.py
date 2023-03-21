from django.db import models

# Create your models here.
class TelegramUser(models.Model):
    telegram_id = models.CharField(max_length=255)
    request_count = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.telegram_id
    

class TelegramComment(models.Model):
    content = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(null=True)

    sn_id = models.CharField(max_length=100, blank=True, null=True)
    user = models.ForeignKey(TelegramUser, blank=True, null=True, on_delete=models.CASCADE)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.content
    

class TelegramSN(models.Model):
    sn = models.CharField(max_length=100, default="not set")
    
    comments = models.ManyToManyField(TelegramComment, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.sn