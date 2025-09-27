# Arquivo: mensagens/views.py
from django.shortcuts import render
from .models import MensagemSecreta
from django.utils import timezone
from django.db.models import Q
import random
from datetime import timedelta
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.http import JsonResponse 

def home_mensagem_secreta(request):
    agora = timezone.now()
    mensagem_para_exibir = None
    
    # 1. Prioridade: Mensagem agendada para hoje
    agendadas_hoje = MensagemSecreta.objects.filter(data_agendada=agora.date()).order_by('?')
    if agendadas_hoje.exists():
        mensagem_para_exibir = agendadas_hoje.first()
        
    # 2. Se não houver agendada, escolhe uma aleatória
    if not mensagem_para_exibir:
        # Pega mensagens não exibidas nas últimas 24 horas
        recentemente_exibidas = agora - timedelta(hours=24)
        candidatas = MensagemSecreta.objects.filter(
            Q(ultima_vez_exibida__isnull=True) | 
            Q(ultima_vez_exibida__lt=recentemente_exibidas)
        ).exclude(data_agendada__isnull=False, data_agendada__lt=agora.date()) # Exclui agendadas passadas
        
        if candidatas.exists():
            # Seleciona de forma randômica
            mensagem_para_exibir = random.choice(list(candidatas)) 
        else:
            # Último recurso: pega a que foi exibida há mais tempo
            mensagem_para_exibir = MensagemSecreta.objects.order_by('ultima_vez_exibida').first()

    # 3. Atualiza o timestamp (se uma mensagem foi selecionada)
    if mensagem_para_exibir:
        mensagem_para_exibir.ultima_vez_exibida = agora
        mensagem_para_exibir.save()
        
    context = {'mensagem': mensagem_para_exibir}
    return render(request, 'mensagens/home.html', context)

@require_POST
def reagir_mensagem(request, mensagem_id):
    """Incrementa a contagem de corações e redireciona de volta para a home."""
    
    # Busca a mensagem pelo ID, ou retorna erro 404 se não encontrar
    mensagem = get_object_or_404(MensagemSecreta, pk=mensagem_id)
    
    # Lógica de incremento
    mensagem.contagem_coracoes += 1
    mensagem.save()
    
    # Redireciona de volta para a página inicial
    # Usamos o redirect para manter o GET e garantir que a página carregue corretamente
    return JsonResponse({'novo_total': mensagem.contagem_coracoes})