# biblioteca/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('catalogo.urls')),  # Asegúrate de que 'catalogo.urls' esté correctamente configurado
]
