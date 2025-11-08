# Início do Código agendamento/models.py

from django.db import models
from pacientes.models import Paciente # Importamos o modelo Paciente
from django.contrib.auth.models import User # Importamos o modelo de Usuário (Médico/Admin)

# Define as opções de status para a consulta
STATUS_CHOICES = [
    ('PENDENTE', 'Pendente de Confirmação'),
    ('CONFIRMADA', 'Confirmada'),
    ('CANCELADA', 'Cancelada'),
    ('REALIZADA', 'Realizada'),
]

# Define a estrutura de dados (tabela) para o Agendamento/Consulta
class Consulta(models.Model):
    # Relacionamento 1:N com Paciente. Uma consulta pertence a um paciente.
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    
    # Relacionamento com o usuário (Admin/Médico). Assumimos 1 médico por enquanto.
    medico = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    # Campo para a data e hora da consulta
    data_hora = models.DateTimeField(unique=True, verbose_name='Data e Hora da Consulta')
    
    # O status da consulta
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='PENDENTE')

    # Campo de registro automático de quando o agendamento foi criado
    data_agendamento = models.DateTimeField(auto_now_add=True)

    # Representação amigável do objeto
    def __str__(self):
        # Exemplo: Consulta com [Nome do Paciente] em [Data]
        return f'Consulta com {self.paciente.nome} em {self.data_hora.strftime("%d/%m/%Y %H:%M")}'

    # Meta (Configurações extras da classe)
    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
        ordering = ['data_hora'] # Ordena a lista de consultas por data

# Fim do Código agendamento/models.py