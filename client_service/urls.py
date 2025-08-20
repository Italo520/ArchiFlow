# client_service/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inclui as rotas do seu app que agora estão em api_urls.py
    path('api/clients/', include('client_service.api_urls')),
]