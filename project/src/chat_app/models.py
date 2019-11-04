from django.db import models

from django.conf import settings
# Create your models here.


class ChanelData(models.Model):
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='chanels'
    )
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)


class MessageData(models.Model):
    chanel = models.ForeignKey('ChanelData', on_delete=models.CASCADE, related_name='messages')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
    message = models.CharField(max_length=255, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)