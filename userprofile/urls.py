from django.urls import path

from . import views as userprofile_views

urlpatterns = [
    path('follow/<int:user_id>', userprofile_views.follow, name='follow'),
    path('unfollow/<int:user_id>', userprofile_views.unfollow, name='unfollow'),
    
    # User Profile
    path('<str:username>/', userprofile_views.user_profile, name='user_profile'),
]
