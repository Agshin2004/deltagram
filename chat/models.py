import uuid
from django.db import models

from authentication.models import User


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants = models.ManyToManyField(related_name='participants', to=User)
    slug = models.SlugField(unique=True, null=True, blank=True)
    
    def __str__(self):
        return f'Par 1: {self.participants.first()}; Par 2: {self.participants.last()}'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = '-'.join(str(id) for id in self.participants.values_list('id', flat=True))
        super().save(*args, **kwargs)
    
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    text = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)
