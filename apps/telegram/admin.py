from django.contrib import admin
from .models import TelegramUser, TelegramComment, TelegramSN

# Register your models here.
admin.site.register(TelegramUser)
admin.site.register(TelegramComment)
admin.site.register(TelegramSN)