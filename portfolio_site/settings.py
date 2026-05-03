import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-default-key-change-it-on-render')

DEBUG = os.environ.get('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = [host.strip() for host in os.environ.get('ALLOWED_HOSTS', '127.0.0.1,localhost,nikhil-portofolio.onrender.com').split(',')]


# Application definition

INSTALLED_APPS = [
    'main.mongo_apps.MongoAdminConfig',
    'main.mongo_apps.MongoAuthConfig',
    'main.mongo_apps.MongoContentTypesConfig',
    'main.mongo_apps.MongoSessionsConfig',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'portfolio_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

MONGODB_URI = os.environ.get('MONGODB_URI', 'localhost')

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_backend',
        'NAME': os.environ.get('MONGODB_NAME', 'portfolio_db'),
        'HOST': MONGODB_URI,
    }
}

# Add Port only if not in URI
if MONGODB_URI == 'localhost':
    DATABASES['default']['PORT'] = 27017


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# WhiteNoise compression and caching
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django_mongodb_backend.fields.ObjectIdAutoField'

MIGRATION_MODULES = {
    "admin": "mongo_migrations.admin",
    "auth": "mongo_migrations.auth",
    "contenttypes": "mongo_migrations.contenttypes",
    "sessions": "mongo_migrations.sessions",
}
