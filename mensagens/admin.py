# Arquivo: mensagens/admin.py
from django.contrib import admin
from .models import MensagemSecreta

@admin.register(MensagemSecreta)
class MensagemSecretaAdmin(admin.ModelAdmin):
    list_display = ('id', 'destinatario', 'data_agendada', 'ultima_vez_exibida', 'texto_curto')
    list_filter = ('destinatario', 'data_agendada')
    search_fields = ('texto',)
    
    # Exibir apenas as 50 primeiras letras na lista
    def texto_curto(self, obj):
        return obj.texto[:50] + '...' if len(obj.texto) > 50 else obj.texto
    texto_curto.short_description = 'Mensagem'