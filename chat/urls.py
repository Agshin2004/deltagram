from django.urls import path

from . import views as chat_views

urlpatterns = [
    path('', chat_views.chat, name='chat'),
    path('<uuid:chat_uuid>/', chat_views.chat_detail, name='chat_detail'),
    path('start_chat/', chat_views.start_chat, name='start_chat'),
]
