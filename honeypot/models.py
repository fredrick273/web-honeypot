

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class IntruderAction(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)
    params = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} on {self.timestamp}"

@receiver(post_save, sender=IntruderAction)
def notify_new_intruder_action(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        message = {
            'ip_address': instance.ip_address,
            'user_agent': instance.user_agent,
            'path': instance.path,
            'timestamp': str(instance.timestamp),
            'params': instance.params,
        }
        async_to_sync(channel_layer.group_send)(
            "intruder_notifications",
            {
                "type": "notify_intruder_action",
                "message": message,
            }
        )
