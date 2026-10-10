# Mensagens do Amor

Aplicação web pessoal que funciona como um cantinho digital privado: a cada visita ela mostra uma
mensagem de carinho, elogio ou motivação, com um tema visual próprio. Foi pensada para o celular
e pode ser salva na tela inicial do iPhone, como se fosse um aplicativo.

## Funcionalidades

- **Mensagens aleatórias:** uma nova mensagem a cada recarregamento, priorizando as que não foram vistas recentemente.
- **Temas visuais:** a cor de fundo e a do botão mudam conforme o tema de cada mensagem.
- **Contador de corações:** dá para reagir a uma mensagem, e a contagem é atualizada na hora, sem recarregar a página.
- **Administração:** as mensagens são cadastradas pelo painel admin do Django.

## Tecnologias

- Python e Django
- Gunicorn e WhiteNoise
- SQLite no desenvolvimento e PostgreSQL em produção
- HTML, CSS responsivo e JavaScript (AJAX)
- Hospedagem no Render

## Como rodar

1. Clone o repositório:

   ```bash
   git clone https://github.com/Glawther/mensagensdoamor.git
   cd mensagensdoamor
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   ```

   No Windows (PowerShell):

   ```powershell
   .\venv\Scripts\Activate
   ```

   No Linux ou macOS:

   ```bash
   source venv/bin/activate
   ```

3. Instale as dependências e crie o banco:

   ```bash
   pip install -r requirements.txt
   python manage.py migrate
   ```

4. Crie o usuário administrador:

   ```bash
   python manage.py createsuperuser
   ```

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

A aplicação fica em `http://127.0.0.1:8000/`. Cadastre as mensagens em `http://127.0.0.1:8000/admin/`.

## Publicação no Render

O projeto está preparado para publicação contínua no Render, que usa o `Procfile`:

```bash
gunicorn MensagensDoAmor.wsgi
```

No painel do Render, defina as variáveis de ambiente `SECRET_KEY` (uma chave longa e aleatória)
e `PYTHON_VERSION`, e inclua o domínio gerado em `ALLOWED_HOSTS` no `settings.py`.

## Licença

Projeto de uso pessoal, com todos os direitos reservados ao autor.
