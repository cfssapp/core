from django.contrib import admin
from .models import Certificate, Comment, CommentImage, Activity, Comment2

# Register your models here.
admin.site.register(Certificate)
admin.site.register(Comment)
admin.site.register(Comment2)
admin.site.register(CommentImage)
admin.site.register(Activity)