❤️ Mensagens do Amor (Sistema de Elogios e Mensagens Secretas)
Sobre o Projeto
Este é um projeto web pessoal construído com Django (Python) e AJAX (JavaScript) para servir como um cantinho digital e privado. O objetivo é fornecer um feed de mensagens de carinho, elogios e motivação de forma aleatória e com temas visuais variados.

O projeto é acessível via celular e foi configurado para ser salvo na tela inicial do iPhone, simulando a experiência de um aplicativo.

Funcionalidades Chave
Mensagens Aleatórias: Exibe uma nova mensagem (elogio ou motivacional) a cada recarregamento da página, baseada em um algoritmo que prioriza mensagens não vistas recentemente.

Temas Visuais: A cor de fundo e do botão mudam dinamicamente com base no tema definido para cada mensagem.

Contador de Corações (AJAX): Permite reagir a uma mensagem clicando no coração (💖). A contagem é atualizada instantaneamente, sem recarregar a página ou mudar a mensagem.

Administração Segura: Todas as mensagens são gerenciadas através do Painel Admin do Django.

🛠️ Tecnologias Utilizadas
Backend: Python 3.x, Django

Servidor WSGI: Gunicorn

Arquivos Estáticos: WhiteNoise

Banco de Dados: SQLite (em desenvolvimento), PostgreSQL (em produção, via Render)

Frontend: HTML, CSS (design responsivo para mobile), JavaScript/AJAX

Hospedagem: Render

🚀 Como Executar Localmente (Desenvolvimento)
Siga estas etapas se você quiser rodar o projeto no seu computador:

Pré-requisitos
Você precisa ter o Python 3 e o Git instalados.

Clone o Repositório:

Bash

git clone https://github.com/Glawther/mensagensdoamor.git
cd mensagensdoamor
Crie e Ative o Ambiente Virtual:

Bash

# Criar
python -m venv venv

# Ativar no Windows (Powershell)
.\venv\Scripts\Activate

# Ativar no Linux/macOS
source venv/bin/activate
Instale as Dependências:

Bash

pip install -r requirements.txt
Configurar o Banco de Dados:

Bash

python manage.py migrate
Criar o Superusuário (Admin):

Bash

python manage.py createsuperuser
Rodar o Servidor:

Bash

python manage.py runserver
O projeto estará acessível em http://127.0.0.1:8000/. Acesse http://127.0.0.1:8000/admin/ para inserir suas mensagens!

☁️ Deploy e Configuração no Render
O projeto está configurado para o deploy contínuo via Render.

Passos de Configuração do Render:
Variáveis de Ambiente (Environment Variables):

SECRET_KEY: (Sua chave secreta longa e segura)

PYTHON_VERSION: (Ex: 3.11.8)

Start Command:
O Render utiliza o Procfile e o comando Gunicorn:

Bash

gunicorn MensagensDoAmor.wsgi
Ambiente de Produção:
Lembre-se de definir a variável SECRET_KEY no painel do Render e de adicionar o domínio gerado (ex: seudominio.onrender.com) na lista ALLOWED_HOSTS do seu settings.py.

📝 Licença
Este projeto é de uso pessoal, com todos os direitos reservados ao autor.

Feito com ❤️ por Glawther
