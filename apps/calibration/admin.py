from django.contrib import admin
from .models import Certificate, Comment, CommentImage

# Register your models here.
admin.site.register(Certificate)
admin.site.register(Comment)
admin.site.register(CommentImage)
# admin.site.register(Activity)