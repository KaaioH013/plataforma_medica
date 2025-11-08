# Início do Código agendamento/admin.py

from django.contrib import admin
from .models import Consulta # Importa a classe Consulta

# Cria uma classe para personalizar como a Consulta será exibida no painel
class ConsultaAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista de consultas
    list_display = ('paciente', 'data_hora', 'status', 'medico', 'data_agendamento')
    
    # Adiciona filtros laterais (ótimo para o médico gerenciar)
    list_filter = ('status', 'medico', 'data_hora')
    
    # Permite buscar por nome do paciente ou status
    search_fields = ('paciente__nome', 'status')
    
    # Permite editar o status diretamente na lista (rápido!)
    list_editable = ('status',)

# Registra a Consulta no painel, usando a customização que criamos
admin.site.register(Consulta, ConsultaAdmin)

# Fim do Código agendamento/admin.py