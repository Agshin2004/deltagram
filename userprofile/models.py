from django.db import models
from django.templatetags.static import static  # The static function is used to generate the URL for static files in the project
from authentication.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(related_name='following', to=User, blank=True)
    followers = models.ManyToManyField(related_name='followers', to=User, blank=True)
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/profile_pictures/', null=True, blank=True)
    last_seen = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_profile_picture(self):
        ''' Return the uploaded profile picture if available, else return the static default image '''
        if self.profile_picture:
            return self.profile_picture.url
        return static('images/default_pp.jpg')  # Path to the default image in static files

    
    
    def __str__(self):
        return f'{self.user.username.capitalize()}\'s Profile'
