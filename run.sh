#!/usr/bin/env bash
# Script para rodar comandos de preparacao antes de iniciar o servidor

# 1. Rodar Migrações
python manage.py migrate --no-input

# 2. Criar Superusuário (Se já existir, o comando retorna sucesso)
python manage.py createsuperuser --no-input --username Glawther --email glawthers@gmail.com --password Dennys147 || true

# 3. Iniciar o Servidor Gunicorn
gunicorn MensagensDoAmor.wsgi:application