# user_service/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # A linha abaixo assume que as rotas de autenticação estão em 'accounts/urls.py'
    path('api/auth/', include('accounts.urls')), 
]