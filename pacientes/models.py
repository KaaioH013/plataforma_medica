# Início do Código pacientes/models.py

from django.db import models

# Define a estrutura de dados (tabela) para o Paciente
class Paciente(models.Model):
    # Campos que o paciente deve ter:
    nome = models.CharField(max_length=150, verbose_name='Nome Completo')
    
    # Email é obrigatório e não pode se repetir
    email = models.EmailField(unique=True) 
    
    # Campo de telefone, permite até 20 dígitos (para incluir DDD/DDI)
    telefone = models.CharField(max_length=20, blank=True, null=True) 
    
    # Data de nascimento
    data_nascimento = models.DateField(blank=True, null=True)
    
    # Campo de histórico conciso (opcional)
    historico = models.TextField(blank=True, null=True, verbose_name='Histórico Médico Breve')

    # Campo de registro automático de quando o paciente foi criado no sistema
    data_cadastro = models.DateTimeField(auto_now_add=True) 

    # Representação amigável do objeto quando for exibido
    def __str__(self):
        return self.nome

    # Meta (Configurações extras da classe)
    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
        ordering = ['nome'] # Ordena a lista de pacientes por nome

# Fim do Código pacientes/models.py