from django.contrib import admin
from .models import Certificate, Comment, CommentImage, Activity

# Register your models here.
admin.site.register(Certificate)
admin.site.register(Comment)
admin.site.register(CommentImage)
admin.site.register(Activity)