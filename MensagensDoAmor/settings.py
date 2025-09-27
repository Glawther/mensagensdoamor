"""
Django settings for MensagensDoAmor project.
"""

from pathlib import Path
import os
from django.conf import settings # Importa o settings (para o bloco de produção)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
# Usa a variável de ambiente SECRET_KEY, com um fallback local para desenvolvimento
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-rnu4#7h)k6o7gjx@!9s0#zk$6c4sg(1r0m#pd#^_%botgx7d7=') 

# SECURITY WARNING: don't run with debug turned on in production!
# Mantenha como True para desenvolvimento local. Mudaremos isso no bloco de produção.
DEBUG = True

# No Render, esta lista deve incluir o domínio do Render. 
# Adicionamos o ".render.com" para cobrir qualquer domínio gerado.
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '.render.com', 'mensagensdoamor-2.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mensagens',
]

MIDDLEWARE = [
    # ----------------------------------------------------
    # NOVO: Middleware do WhiteNoise (DEVE VIR LOGO ABAIXO DO SecurityMiddleware)
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    # ----------------------------------------------------
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'MensagensDoAmor.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'MensagensDoAmor.wsgi.application'


# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization

LANGUAGE_CODE = 'pt-br' # Alterado para português
TIME_ZONE = 'America/Sao_Paulo' # Alterado para o fuso horário mais comum no Brasil

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# Diretório onde o Django irá COLETAR os arquivos estáticos para produção
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') 

# Default primary key field type

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# =========================================================================
# CONFIGURAÇÕES PARA AMBIENTE DE PRODUÇÃO (RENDER)
# =========================================================================

# Checa se está no ambiente de produção (se DEBUG for False)
if not DEBUG:

    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    # 1. Força a desativação de debug (CRÍTICO)
    DEBUG = False 
    
    # 2. Configura WhiteNoise para servir arquivos estáticos
    # Isso comprime os arquivos e garante que o navegador os armazene em cache.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' 
    
    # 3. Permite o acesso seguro (HTTPS)
    # Isso garante que o Render rode seu site de forma segura.
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')