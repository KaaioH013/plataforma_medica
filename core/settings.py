# Início do Código Completo core/settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o#w&t7&x2y8m%o#9m-3(h*@o-w_q7p-1p$m-o6-8x6k-k!n*8)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Meus Apps
    'pacientes',  # <-- O seu App Pacientes
    'agendamento',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# A seção que precisava ser corrigida/restaurada:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': BASE_DIR / 'db.sqlite3', 
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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

# Início do Código core/settings.py (Seção TEMPLATES ATUALIZADA)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Aqui dizemos ao Django para procurar templates na pasta BASE_DIR/templates
        'DIRS': [BASE_DIR / 'templates'], 
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Fim do Código core/settings.py (Seção TEMPLATES ATUALIZADA)

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-br' # Usando Português do Brasil

TIME_ZONE = 'America/Sao_Paulo' # Usando Fuso de São Paulo

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Fim do Código Completo core/settings.py

# Início do Código core/settings.py (ADICIONAR AO FINAL)

# ... (código que define STATIC_URL = 'static/')

# Adiciona o caminho para a pasta 'static' que acabamos de criar
import os 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]

# Início do Código core/settings.py (Seção de Arquivos Estáticos)

# ... (código anterior)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Diretório onde o Django deve COLETAR todos os arquivos estáticos (APENAS EM PRODUÇÃO)
STATIC_ROOT = BASE_DIR / 'staticfiles' # <--- LINHA ESSENCIAL ADICIONADA AQUI

# Diretórios onde o Django DEVE PROCURAR arquivos estáticos durante o desenvolvimento
import os 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'), 
]

# Default primary key field type
# ...

# Fim do Código core/settings.py (Seção de Arquivos Estáticos)
# Fim do Código core/settings.py
# Início do Código core/settings.py (NOVAS CONFIGURAÇÕES DE I18N/L10N)

# ... (código anterior)

# Configurações de localização e internacionalização para o Brasil
USE_L10N = True

# Define o formato esperado para data e hora no Brasil
DATETIME_INPUT_FORMATS = ['%d/%m/%Y %H:%M', '%d/%m/%Y', '%Y-%m-%d %H:%M:%S'] 
DATE_INPUT_FORMATS = ['%d/%m/%Y', '%Y-%m-%d', '%d%m%Y'] # <--- ISSO PERMITE DD/MM/AAAA E DDMMAAAA

# Fim do Código core/settings.py