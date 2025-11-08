# Início do Código pacientes/admin.py

from django.contrib import admin
from .models import Paciente # Importa a classe Paciente do nosso models.py

# Registra o seu modelo no painel de administração.
# O médico/administrador agora poderá gerenciar pacientes por lá.
admin.site.register(Paciente)

# Fim do Código pacientes/admin.py