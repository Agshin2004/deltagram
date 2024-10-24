from django.db import models
from authentication.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # ID 1 is an admin)
    title = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    image = models.ImageField(upload_to='images/post/')
    like = models.ManyToManyField(related_name='likes', to=User)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
