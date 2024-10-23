from django.db.models.signals import post_save

from authentication.models import User
from . models import Profile


# Receiver function will be called when the signal is sent (User objects got created in this case)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()


post_save.connect(create_profile, User)