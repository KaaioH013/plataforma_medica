# Início do Código pacientes/urls.py

from django.urls import path
from . import views 

app_name = 'pacientes' 

urlpatterns = [
    # Mapeamento para a Home Page
    path('', views.home, name='home'),
    
    # Mapeamento para a Página de Cadastro de Paciente
    path('cadastro/', views.cadastrar_paciente, name='cadastro_paciente'), # <-- NOVO PATH
]

# Fim do Código pacientes/urls.py