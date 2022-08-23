"""
Django settings for restfulapicrud project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

# import os
from pathlib import Path
# import environ #　django-environ-2をインポート
import dj_database_url
from dotenv import (
    find_dotenv,
    load_dotenv,
)


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# .envファイルを読み込み
# env = environ.Env()
# environ.Env.read_env(Path.joinpath(BASE_DIR, '.env')) # ここで.envファイルを読み込み


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ttyejeg@xqmr#^16y=2(q%jl(l5rfn#*(pjtzfux311#inyay$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'foodapi',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'restfulapicrud.urls'

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

WSGI_APPLICATION = 'restfulapicrud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'cc_guluten_django',
#         'USER': 'sadakiawada',
#         'PASSWORD': 'p2lduhsq',
#         'HOST': 'localhost'
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd8nn85i7ikaje0',
#         'HOST': 'ec2-52-207-15-147.compute-1.amazonaws.com',
#         'PORT': '5432',
#         'USER': 'njuuzpdblvqidc',
#         'PASSWORD': '0bc30851afef4e25c5c3f7f8c2913ef9cb68cc6e6dd4b31fff3355418d94d28d',

#     }
# }

# DATABASES = {
#     # os.environ['DATABASE_URL']を読み込みます。なければImproperlyConfigured例外が発生します
#     'default': env.db() ,
#     # os.environ['SQLITE_URL']を読み込みます

# }

import dj_database_url
# from dotenv import (
#     find_dotenv,
#     load_dotenv,
# )
# load_dotenv(find_dotenv())
DATABASES = { 'default': dj_database_url.config(default='postgres://njuuzpdblvqidc:0bc30851afef4e25c5c3f7f8c2913ef9cb68cc6e6dd4b31fff3355418d94d28d@ec2-52-207-15-147.compute-1.amazonaws.com:5432/d8nn85i7ikaje0') }
# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600),
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'd8nn85i7ikaje0'
#     }
# }


# # import dj_databse_url
# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)

ALLOWED_HOSTS = ['*']

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ALLOWED_ORIGINS = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
    'https://guluten-free-life-django.herokuapp.com'
]

CORS_ORIGIN_WHITELIST = [
     'http://127.0.0.1:3000',
     'http://localhost:3000',
     'https://guluten-free-life-django.herokuapp.com',

]

# CORS_ALLOW_CREDENTIALS = True

# WHITENOISE_ALLOW_ALL_ORIGINS = False

CORS_ORIGIN_ALLOW_ALL=True