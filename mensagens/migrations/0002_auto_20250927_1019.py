# Arquivo: mensagens/migrations/0002_auto_20250927_1019.py

from django.db import migrations

# =========================================================
# 1. DADOS ESTÁTICOS DAS FRASES
# =========================================================
FRASES_INICIAIS = [
    # FRASES DE AMOR (E)
    {"texto": "Seu riso é minha música preferida. Nunca pare de me dar esse som.", "destinatario": "E", "tema_cor": "verde"},
    {"texto": "Em um universo de bilhões, você é meu lugar favorito. Em casa ou em qualquer lugar.", "destinatario": "E", "tema_cor": "azul"},
    {"texto": "Você é a minha história de amor perfeita. Amo te viver!", "destinatario": "E", "tema_cor": "rosa"},
    {"texto": "Só de você existir, já ilumina o meu dia. Não é o que você faz, é quem você é.", "destinatario": "E", "tema_cor": "amarelo"},
    {"texto": "Amar você é como respirar: essencial, fácil e constante.", "destinatario": "E", "tema_cor": "rosa"},
    {"texto": "Tudo o que eu tenho e tudo o que eu sou, é seu", "destinatario": "E", "tema_cor": "amarelo"},
    {"texto": "Você é a minha pessoa favorita. Eu te amo!", "destinatario": "E", "tema_cor": "rosa"},
    
    
    # FRASES MOTIVACIONAIS (M)
    {"texto": "Confie na sua voz. O ato mais corajoso é pensar por você mesma.", "destinatario": "M", "tema_cor": "verde"},
    #{"texto": "Seja como o oceano: calma por fora, mas cheia de força e mistério por dentro.", "destinatario": "M", "tema_cor": "azul"},
    #{"texto": "Não existem limites para aquilo que nós, mulheres, conseguimos alcançar. Acredite nisso.", "destinatario": "M", "tema_cor": "verde"},
    {"texto": "Você deve lutar mais de uma batalha para se tornar uma vencedora. E você tem a força.", "destinatario": "M", "tema_cor": "amarelo"},
    {"texto": "A elegância é quando o interior é tão belo quanto o exterior. Seja linda, seja você.", "destinatario": "M", "tema_cor": "rosa"},
]


def inserir_frases_iniciais(apps, schema_editor):
    MensagemSecreta = apps.get_model('mensagens', 'MensagemSecreta')
    
    for frase_data in FRASES_INICIAIS:
        MensagemSecreta.objects.create(**frase_data)
# =========================================================
# FIM DOS DADOS ESTÁTICOS
# =========================================================


class Migration(migrations.Migration):

    dependencies = [
        # Isso garante que ele dependa da migração que cria a tabela
        ('mensagens', '0001_initial'), 
    ]

    operations = [
        # Executa a função de inserção de dados
        migrations.RunPython(inserir_frases_iniciais),
    ]