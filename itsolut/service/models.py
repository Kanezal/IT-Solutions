import uuid
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_key_model(sender, instance, created, **kwargs):
    if created:
        KeyModel.objects.create(user=instance, key=str(uuid.uuid4()))

class KeyModel(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='key')
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.api_key
    