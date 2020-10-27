from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

POSTGRESQL = {
    'default': {

        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        'NAME': 'postgres',

        'USER': 'postgres_admin',

        'PASSWORD': '23596817idk',

        'HOST': 'database-1.cqs3azbh70tm.us-east-1.rds.amazonaws.com',

        'PORT': '5432',

    }
}
