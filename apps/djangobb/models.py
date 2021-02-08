from django.db import models
from django.conf import settings

Create your models here.
class Topic(models.Model):
    forum = models.ForeignKey(Forum, related_name='topics', verbose_name=_('Forum'))
    name = models.CharField(_('Subject'), max_length=255)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'))
    views = models.IntegerField(_('Views count'), blank=True, default=0)
    post_count = models.IntegerField(_('Post count'), blank=True, default=0)

    def __str__(self):
        return self.name