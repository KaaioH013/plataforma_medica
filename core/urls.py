# Início do Código core/urls.py

from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    # Mapeia a URL /admin para o painel administrativo do Django
    path('admin/', admin.site.urls), 
    
    # Mapeia a URL inicial ('') para o nosso App pacientes
    path('', include('pacientes.urls')), 
    
    # Mapeia as URLs de agendamento (ex: /agendar/)
    path('', include('agendamento.urls')), # <-- NOVO INCLUDE AQUI!
]

# Fim do Código core/urls.py