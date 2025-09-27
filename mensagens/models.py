# Arquivo: mensagens/models.py
from django.db import models

class MensagemSecreta(models.Model):
    texto = models.TextField(verbose_name="Elogio/Mensagem") 
    
    DESTINATARIO_CHOICES = [
        ('E', 'Ela'),
        ('N', 'Nós'),
        ('M', 'Motivacional') # Adicionei mais uma opção
    ]
    destinatario = models.CharField(
        max_length=1, 
        choices=DESTINATARIO_CHOICES, 
        default='E',
        verbose_name="Para Quem?"
    )
    
    TEMA_CHOICES = [
        ('rosa', 'Rosa Suave'),
        ('azul', 'Azul Sereno'),
        ('verde', 'Verde Calmo'),
        ('amarelo', 'Amarelo Quente'),
    ]
    tema_cor = models.CharField(
        max_length=10,
        choices=TEMA_CHOICES,
        default='rosa',
        verbose_name="Tema de Cor"
    )

    contagem_coracoes = models.PositiveIntegerField(
        default=0,
        verbose_name="Contagem de Corações"
    )

    data_agendada = models.DateField(
        null=True, 
        blank=True,
        verbose_name="Agendar para o dia"
    )
    
    ultima_vez_exibida = models.DateTimeField(
        null=True, 
        blank=True,
        verbose_name="Última exibição"
    ) 

    class Meta:
        verbose_name = "Mensagem Secreta"
        verbose_name_plural = "Mensagens Secretas"

    def __str__(self):
        return f"Msg {self.id} | {self.get_destinatario_display()}: {self.texto[:30]}..."