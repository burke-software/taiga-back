from .development import *

DATABASES = {
    'default': {
        'ENGINE': 'transaction_hooks.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}

BROKER_URL = 'amqp://guest:guest@amqp:5672//'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
