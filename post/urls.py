from django.urls import path

from . import views as post_views

urlpatterns = [
    path('add_post', post_views.add_post, name='add_post'),
    path('remove_post/<int:post_id>/', post_views.remove_post, name='remove_post'),
    path('post_detail/<int:post_id>/', post_views.post_detail, name='post_detail'),
    path('like_or_dislike_post/<int:post_id>/', post_views.like_or_dislike_post, name='like_or_dislike_post'),
]