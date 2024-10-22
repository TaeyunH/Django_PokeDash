from django.contrib import admin
from django.urls import path, include  # Import 'include' for app URL inclusion
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', include('space_tigersapp.urls')),  # Include URLs from the space_tigersapp app
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth URLs (login, logout, password reset, etc.)
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

