from django.contrib import admin
from django.urls import path, include

from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('authentication/', include('authentication.urls')),
]
