from . models import Profile
from django.db.models.signals import post_save
from django.core.signals import request_finished
from authentication.models import User

from datetime import datetime

# Receiver function will be called when the signal is sent (User objects got created in this case)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile.objects.create(user=instance)
        user_profile.save()


def update_last_seen(sender, instance, **kwargs):
    print(instance)
    print('update_last_seen')
    user_profile = Profile.objects.filter(user=instance)
    user_profile.update(last_seen=datetime.now())

post_save.connect(create_profile, User)
request_finished.connect(update_last_seen, User)
