

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.TimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)




    def __str__(self):
        return (self.message)
class Meta:
    ordering = ['-timestamp']

class Imagen(models.Model):
    image = models.ImageField(upload_to="foto", null=True)

