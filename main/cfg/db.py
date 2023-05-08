def get_db_cfg(postgres, base_dir, postgres_instance):
    if postgres == "postgres-on":
        return {
            'default': {
                'ENGINE': postgres_instance.DATABASE_ENGINE,
                'NAME': postgres_instance.DATABASE_DATABASE,
                'USER': postgres_instance.DATABASE_USERNAME,
                'PASSWORD': postgres_instance.DATABASE_PASSWORD,
                'HOST': postgres_instance.DATABASE_HOST,
                'PORT': postgres_instance.DATABASE_PORT,
            }
        }
    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': base_dir / 'db.sqlite3',
        }
    }
