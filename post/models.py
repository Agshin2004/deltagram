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

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    
    def __str__(self):
        return f'{self.user.username}\'s comment on {self.post}'
    