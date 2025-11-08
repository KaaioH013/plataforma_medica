# Início do Código agendamento/forms.py

from django import forms
# Note: Não importamos mais o modelo Consulta, pois o formulário agora é customizado
# from .models import Consulta 

# Formulário customizado, sem herdar de ModelForm
class AgendamentoForm(forms.Form):
    # Campo para o paciente se identificar. Usaremos o email.
    email_paciente = forms.EmailField(
        label='Seu E-mail (o mesmo usado no cadastro)',
        help_text='Usaremos este e-mail para buscar seu cadastro e enviar a confirmação.',
        widget=forms.EmailInput(attrs={'class': 'form-control'}) # Classe Bootstrap
    )
    
    # Campo oculto (hidden) que será preenchido com o horário que o paciente clicar
    slot_horario = forms.CharField(widget=forms.HiddenInput(), required=False)


# Fim do Código agendamento/forms.py