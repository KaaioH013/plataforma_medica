# Início do Código pacientes/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PacienteForm # Importa o formulário que acabamos de criar

# ----------------------------------------------------
# 1. View da Home Page
# ----------------------------------------------------
def home(request):
    return render(request, 'base.html')


# ----------------------------------------------------
# 2. View para Cadastrar um Novo Paciente (Frontend)
# ----------------------------------------------------
def cadastrar_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        
        if form.is_valid():
            form.save() # Salva os dados no banco de dados
            messages.success(request, 'Cadastro realizado com sucesso! Você pode agendar sua consulta agora.')
            
            # REDIRECIONAMENTO CORRIGIDO: Envia diretamente para a página de agendamento
            return redirect('agendamento:agendar_consulta') 
        else:
            # Se o formulário for inválido, exibe os erros explícitos.
            # O .as_text() é uma técnica para exibir os erros do formulário em uma string.
            for field, errors in form.errors.items():
                 for error in errors:
                     messages.error(request, f'{form.fields[field].label}: {error}')

    else:
        form = PacienteForm() # Cria um formulário vazio para exibição

    # Renderiza o template, enviando o formulário para ser exibido
    return render(request, 'cadastro_paciente.html', {'form': form})

# Fim do Código pacientes/views.py