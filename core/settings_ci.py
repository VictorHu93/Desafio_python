from .settings import *  # Importa todas as configurações padrão

# Define o banco de dados como SQLite em memória para testes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
