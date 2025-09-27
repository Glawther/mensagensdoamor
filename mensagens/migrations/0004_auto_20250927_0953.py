# Arquivo: mensagens/migrations/000X_seunome.py

from django.db import migrations

# Dados das frases (usando a estrutura do seu modelo)
# tema_cor: rosa, azul, verde, amarelo.
# destinatario: E (Ela), M (Motivacional).
FRASES_INICIAIS = [
    # FRASES DE AMOR (E)
    {"texto": "Seu riso é minha música preferida. Nunca pare de me dar esse som.", "destinatario": "E", "tema_cor": "rosa"},
    {"texto": "Em um universo de bilhões, você é meu lugar favorito. Em casa ou em qualquer lugar.", "destinatario": "E", "tema_cor": "azul"},
    {"texto": "Você é a minha história de amor perfeita. Amo te viver!", "destinatario": "E", "tema_cor": "amarelo"},
    {"texto": "Só de você existir, já ilumina o meu dia. Não é o que você faz, é quem você é.", "destinatario": "E", "tema_cor": "amarelo"},
    {"texto": "Amar você é como respirar: essencial, fácil e constante.", "destinatario": "E", "tema_cor": "rosa"},
    {"texto": "Tudo o que sou e tudo o que eu tenho é seu.", "destinatario": "E", "tema_cor": "verde"},
    {"texto": "Você é minha pessoa favorita. Eu te amo!", "destinatario": "E", "tema_cor": "amarelo"},


    # FRASES MOTIVACIONAIS (M)
    {"texto": "Confie na sua voz. O ato mais corajoso é pensar por você mesma.", "destinatario": "M", "tema_cor": "verde"},
    {"texto": "Você deve lutar mais de uma batalha para se tornar uma vencedora. E você tem a força.", "destinatario": "M", "tema_cor": "amarelo"},
    {"texto": "A elegância é quando o interior é tão belo quanto o exterior. Seja linda, seja você.", "destinatario": "M", "tema_cor": "rosa"},
]


def inserir_frases_iniciais(apps, schema_editor):
    MensagemSecreta = apps.get_model('mensagens', 'MensagemSecreta')

    for frase_data in FRASES_INICIAIS:
        MensagemSecreta.objects.create(**frase_data)


class Migration(migrations.Migration):

    dependencies = [
        ('mensagens', '0003_auto_20250927_0830'), # Mantenha a última migração do seu projeto aqui!
    ]

    operations = [
        migrations.RunPython(inserir_frases_iniciais),
    ]