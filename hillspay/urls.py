from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from home.views import home

urlpatterns = [
	path('', home, name='home'),
	path('home/', include('home.urls', namespace='home')),
	path('chat/', include('chat.urls', namespace='chat')),
	path('users/', include('users.urls', namespace='users')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
