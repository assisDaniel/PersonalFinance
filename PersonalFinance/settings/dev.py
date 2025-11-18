import os
from .base import *

#
DEBUG = True
#
ALLOWED_HOSTS = []
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
]
CORS_ALLOWED_ORIGINS = CSRF_TRUSTED_ORIGINS

################

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.parent / 'db.sqlite3',
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

# Diretório onde os arquivos estáticos serão coletados quando rodar 'collectstatic'
# Usado em produção para servir todos os arquivos estáticos de um único lugar
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# URL base para acessar arquivos estáticos no navegador
# Ex: um arquivo em STATIC_ROOT será acessível em /PersonalFinance/static/arquivo.css
STATIC_URL = '/PersonalFinance/static/'

# Lista de diretórios adicionais onde o Django procura arquivos estáticos durante o desenvolvimento
# Esses arquivos serão copiados para STATIC_ROOT quando rodar 'collectstatic'
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"),  # Comentado para evitar duplicação com STATIC_ROOT
    os.path.join(BASE_DIR.parent, "static-global/"),  # Pasta de estáticos compartilhados entre projetos
]

# URL base para acessar arquivos de mídia (uploads de usuários) no navegador
# Ex: uma imagem enviada será acessível em /media/imagem.jpg
MEDIA_URL = '/media/'

# Diretório físico onde os arquivos enviados pelos usuários serão armazenados
# Fica um nível acima do projeto para ser compartilhado entre diferentes aplicações
MEDIA_ROOT = os.path.join(BASE_DIR.parent, 'media')
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases