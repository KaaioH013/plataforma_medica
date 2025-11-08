# Início do Código agendamento/urls.py

from django.urls import path
from . import views 

app_name = 'agendamento' # Define um nome para este App

urlpatterns = [
    # Mapeamento para a Página de Agendamento
    path('agendar/', views.agendar_consulta, name='agendar_consulta'), 
]

# Fim do Código agendamento/urls.py