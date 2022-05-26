from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('api/', include('api.urls')),
    path('admin/', admin.site.urls),
    path(r'auth/', include('djoser.urls')),
    path(r'auth/', include('djoser.urls.authtoken')),
    path(r'auth/', include('djoser.urls.jwt')),
    path(r'swagger/', schema_view),
    path(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path(r'debug-toolbar/', include('debug_toolbar.urls')),
]
