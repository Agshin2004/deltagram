from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class UserAdmin(admin.ModelAdmin):
    fields = ['user', 'profile_picture', 'bio', 'followers', 'following', 'last_seen', 'date_created', 'date_modified']
    readonly_fields = ['last_seen', 'date_created', 'date_modified']

