from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

POSTGRESQL = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'smartipdb',
    'USER': 'postgres',
    'PASSWORD': 'adminTecnicos',
    'HOST': 'localhost',
    'PORT': '5432'
    }
}