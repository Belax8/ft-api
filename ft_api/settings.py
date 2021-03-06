"""
Django settings for ft_api project.

Generated by 'django-admin startproject' using Django 1.9.7

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from configurations import Configuration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Base(Configuration):

    STORED_PROCEDURES = BASE_DIR + '/db_objects/stored_procedures/'
    EMAIL_TEMPLATES = BASE_DIR + '/ft_api/templates/email/'

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'sc8e*js2k@mbhul&2%stb5ap4%%3c#vj_4(d**fout@@#tf_s2'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = ['127.0.0.1']

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'corsheaders',
        'rest_framework.authtoken',
        'rest_framework',
        'rest_framework_signature',
        'django_nose',
        'ft_api.apps.FtApiConfig'
    ]

    MIDDLEWARE_CLASSES = [
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    # Rest_framework config
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'rest_framework_signature.authentication.TokenAuthentication',
        ),
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        )
    }

    # CORS Settings
    CORS_ORIGIN_ALLOW_ALL = True
    CORS_ALLOW_CREDENTIALS = True
    CORS_ALLOW_HEADERS = (
        'Content-Type',
        'x-ft-super-key',
        'Authorization',
        'x-ft-api-key',
        'x-ft-api-nonce',
        'x-ft-timestamp'
    )

    ROOT_URLCONF = 'ft_api.urls'

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

    WSGI_APPLICATION = 'ft_api.wsgi.application'

    # Password validation
    # https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
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
    # https://docs.djangoproject.com/en/1.9/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
    NOSE_ARGS = [
        '--with-coverage',
        '--cover-package=ft_api'
    ]

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.9/howto/static-files/
    STATIC_URL = '/static/'

    AUTHENTICATION_BACKENDS = (
        'rest_framework_signature.backend.MSSQLBackend',
    )

    REST_FRAMEWORK_SIGNATURE = {
        'SUPER_KEY_AUTH': 'ft-test-cp',
        'DATABASE_ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER_DOCUMENT': 'ft_api.domain.models.User',
        'APPLICATION_DOCUMENT': 'ft_api.domain.models.ApiKey',
        'AUTH_TOKEN_DOCUMENT': 'ft_api.domain.models.AuthToken',
        'API_PERMISSION_MODEL': 'ft_api.domain.models.ApiPermission',
        'SUPER_KEY_HEADER': 'HTTP_X_FT_SUPER_KEY',
        'TIMESTAMP_HEADER': 'HTTP_X_FT_TIMESTAMP',
        'NONCE_HEADER': 'HTTP_X_FT_API_NONCE',
        'API_KEY_HEADER': 'HTTP_X_FT_API_KEY',
        'DISABLE_USER_AUTH': True,
        'BYPASS_URLS': [
        ],
        'SSO_TOKEN_CLASSES': [
        ],
        'FULL_ACCESS_API_KEY_NAMES': ['ft-app', 'test-app'],
        'MULTIPART_POST_URLS': [],
        'UNSECURED_URLS': []
    }


class Local(Base):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fitness_tracker_local',
            'USER': 'ft',
            'PASSWORD': 'test1234',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }


class Dev(Base):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fitness_tracker_dev',
            'USER': 'ft',
            'PASSWORD': 'test1234',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }


class Prod(Base):

    DEBUG = False

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'fitness_tracker_prod',
            'USER': 'ft',
            'PASSWORD': 'test1234',
            'HOST': 'localhost',
            'PORT': '5432'
        }
    }
