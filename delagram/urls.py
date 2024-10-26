from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from delagram import settings

from . import views as main_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.home, name='home'),
    path('authentication/', include('authentication.urls')),
    path('profile/', include('userprofile.urls')),
    path('post/', include('post.urls')),
    path('chat/', include('chat.urls')),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
