# Início do Código agendamento/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta, datetime, time, date 
from .forms import AgendamentoForm
from pacientes.models import Paciente 
from .models import Consulta 


# --- FUNÇÃO AUXILIAR: Encontra o Próximo Dia Livre (PULANDO FINAIS DE SEMANA) ---
def find_proximo_dia_livre(dia_inicial):
    hoje = timezone.now().date()
    current_day = max(dia_inicial.date(), hoje) 
    
    for _ in range(180):
        # NOVO: Se for Sábado (5) ou Domingo (6), pula para Segunda
        while current_day.weekday() >= 5: # 5=Sábado, 6=Domingo
            current_day += timedelta(days=1)

        # Gera todos os slots possíveis para o dia
        horarios = get_horarios_disponiveis(datetime.combine(current_day, time(0, 0)))

        if horarios:
            return current_day
        
        # Avança para o próximo dia
        current_day += timedelta(days=1)
        
    return dia_inicial.date()


# --- FUNÇÃO AUXILIAR: Gera os slots disponíveis para o dia (Inclui validação de fim de semana) ---
def get_horarios_disponiveis(dia):
    # NOVO: Se o dia for fim de semana, retorna lista vazia imediatamente.
    if dia.weekday() >= 5:
        return []

    HORA_INICIO = 9
    HORA_FIM = 17
    INTERVALO_MINUTOS = 30 

    horarios_totais = []
    
    hora_atual_naive = datetime.combine(dia.date(), time(HORA_INICIO, 0))
    hora_final_naive = datetime.combine(dia.date(), time(HORA_FIM, 0))

    hora_atual = timezone.make_aware(hora_atual_naive)
    hora_final = timezone.make_aware(hora_final_naive)
    
    while hora_atual <= hora_final:
        if hora_atual > timezone.now(): 
            horarios_totais.append(hora_atual)
        hora_atual += timedelta(minutes=INTERVALO_MINUTOS)

    consultas_ocupadas = Consulta.objects.filter(
        data_hora__date=dia.date()
    ).values_list('data_hora', flat=True) 

    horarios_ocupados = [timezone.localtime(dt) for dt in consultas_ocupadas]

    horarios_disponiveis = [
        dt.strftime("%H:%M") 
        for dt in horarios_totais 
        if dt not in horarios_ocupados
    ]
    
    return horarios_disponiveis


# --- VIEW DE AGENDAMENTO (PRINCIPAL) (Mantida) ---
def agendar_consulta(request):
    hoje = timezone.now().date() 
    
    dia_selecionado = request.GET.get('dia')

    if dia_selecionado:
        try:
            dia_dt = datetime.strptime(str(dia_selecionado), '%Y-%m-%d')
        except ValueError:
            dia_dt = datetime.combine(hoje, time(0,0))
    else:
        # 2. Se não houver dia na URL (primeiro acesso), encontra o próximo dia livre
        dia_livre = find_proximo_dia_livre(datetime.combine(hoje, time(0,0)))
        dia_dt = datetime.combine(dia_livre, time(0,0))

    # --- O RESTANTE DA LÓGICA DE NAVEGAÇÃO E PROCESSAMENTO É MANTIDO ---
    disponibilidade = get_horarios_disponiveis(dia_dt)
    
    data_anterior = (dia_dt - timedelta(days=1)).strftime('%Y-%m-%d')
    data_proxima = (dia_dt + timedelta(days=1)).strftime('%Y-%m-%d')
    semana_anterior = (dia_dt - timedelta(weeks=1)).strftime('%Y-%m-%d')
    semana_proxima = (dia_dt + timedelta(weeks=1)).strftime('%Y-%m-%d')
    
    
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        
        email = request.POST.get('email_paciente')
        slot_horario_str = request.POST.get('slot_horario')
        
        # Converte a data e garante a consciência de fuso horário
        data_hora_agendamento = timezone.make_aware(datetime.strptime(
            f'{dia_dt.strftime("%Y-%m-%d")} {slot_horario_str}', 
            '%Y-%m-%d %H:%M'
        ))
        
        # --- Lógica de Validação e Salvamento ---
        
        try:
            paciente = Paciente.objects.get(email=email)
        except Paciente.DoesNotExist:
            messages.error(request, 'Erro: Seu e-mail não está cadastrado. Por favor, cadastre-se primeiro.')
            return render(request, 'agendar_consulta.html', {
                'form': form, 'disponibilidade': disponibilidade, 'dia_atual': dia_dt,
                'data_anterior': data_anterior, 'data_proxima': data_proxima,
                'semana_anterior': semana_anterior, 'semana_proxima': semana_proxima,
            })

        if data_hora_agendamento < timezone.now():
            messages.error(request, 'Erro: Você não pode agendar consultas para datas no passado.')
        elif slot_horario_str not in disponibilidade:
            messages.error(request, 'Erro: Este horário não está disponível ou é inválido.')
        else:
            Consulta.objects.create(
                paciente=paciente,
                data_hora=data_hora_agendamento,
                status='PENDENTE' 
            )

            messages.success(request, f'Consulta agendada com sucesso para {data_hora_agendamento.strftime("%d/%m/%Y às %H:%M")}. Status: Pendente.')
            return redirect('pacientes:home')
            
    else: # GET request
        form = AgendamentoForm() 

    # Renderiza o template
    return render(request, 'agendar_consulta.html', {
        'form': form, 
        'disponibilidade': disponibilidade, 
        'dia_atual': dia_dt,
        'data_anterior': data_anterior,
        'data_proxima': data_proxima,
        'semana_anterior': semana_anterior, 
        'semana_proxima': semana_proxima, 
    })

# Fim do Código agendamento/views.py