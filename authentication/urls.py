from django.urls import path

from . import views as auth_views

urlpatterns = [
    path('register/', auth_views.register_view, name='register'),
    path('login/', auth_views.login_view, name='login'),
    path('logout/', auth_views.logout_view, name='logout')
]