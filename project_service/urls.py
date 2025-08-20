# project_service/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Esta linha direciona tudo que chegar em /api/projects/
    # para o seu arquivo de rotas da API (que você renomeou para api_urls.py).
    path('api/projects/', include('project_service.api_urls')),
]