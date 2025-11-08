# Início do Código pacientes/forms.py (SOLUÇÃO DE BYPASS)

from django import forms
from .models import Paciente
from datetime import datetime
from django.core.exceptions import ValidationError 

# Cria um formulário baseado no modelo Paciente
class PacienteForm(forms.ModelForm):
    # CORREÇÃO DEFINITIVA: Sobrescreve o campo do modelo para ser um simples campo de texto no formulário.
    # Isso desativa a validação rígida do HTML5/Django para o DateField.
    data_nascimento = forms.CharField(
        label='Data de Nascimento',
        widget=forms.TextInput(attrs={'placeholder': 'DDMMAAAA ou DD/MM/AAAA', 'class': 'form-control'})
    )

    class Meta:
        model = Paciente
        # Note que data_nascimento ainda está na lista de fields
        fields = ['nome', 'email', 'telefone', 'data_nascimento', 'historico']

        labels = {
            'nome': 'Nome Completo',
            'email': 'E-mail (Será seu login)',
            'telefone': 'Telefone (com DDD)',
            'historico': 'Histórico Médico Breve (Opcional)',
        }
    
    # O clean_data_nascimento ainda é necessário para converter a string de texto para o objeto Date que o modelo espera.
    def clean_data_nascimento(self):
        data_str = self.cleaned_data.get('data_nascimento')
        
        if not data_str and not self.fields['data_nascimento'].required:
             return None

        # 1. Remove qualquer caractere que não seja número
        data_limpa = ''.join(filter(str.isdigit, str(data_str)))

        # 2. Tenta formatar (se for 8 dígitos: DDMMYYYY)
        if len(data_limpa) == 8:
            try:
                data_objeto = datetime.strptime(data_limpa, '%d%m%Y').date()
                return data_objeto
            except ValueError:
                raise ValidationError(
                    'Formato de data inválido. Use 8 dígitos (DDMMAAAA) ou o formato padrão: DD/MM/AAAA.'
                )
        
        # 3. Se não for 8 dígitos exatos, lança o erro explícito
        raise ValidationError(
            'Formato inválido. Por favor, digite a data como DDMMAAAA (Ex: 26101996) ou DD/MM/AAAA.'
        )

# Fim do Código pacientes/forms.py