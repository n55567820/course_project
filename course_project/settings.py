"""
Django settings for course_project project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

stage = os.environ.get("STAGE")
docker_dev_stage = 'DOCKER-DEV'
pro_stage = 'Product'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production! 
DEBUG = True

ALLOWED_HOSTS = ['*']


# +------+
# | Apps |
# +------+
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "django_extensions",
    "rest_framework",
    "drf_yasg",
    "django_filters",
    'corsheaders',

    'courses',
    'jwtauth',
]

REST_FRAMEWORK = {
  'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',],
  'DEFAULT_PARSER_CLASSES': ['rest_framework.parsers.JSONParser',],
  'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.SessionAuthentication','rest_framework_simplejwt.authentication.JWTAuthentication',],
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
]

SWAGGER_SETTINGS = {
  'DEFAULT_MODEL_RENDERING': 'example',
  'SHOW_COMMON_EXTENSIONS': False,
  'DISPLAY_OPERATION_ID': False,
  'USE_SESSION_AUTH': True,
}

ROOT_URLCONF = 'course_project.urls'

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.joinpath("templates")
        ],
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

WSGI_APPLICATION = 'course_project.wsgi.application'


# +----------+
# | Database |
# +----------+
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',  #PostgreSQL
        'NAME': 'course-project',  #資料庫名稱
        'USER': os.environ.get("COURSE_PROJECT_POSTGRES_USER"),  #資料庫帳號
        'PASSWORD': os.environ.get("COURSE_PROJECT_POSTGRES_PASSWORD"),  #資料庫密碼
        'HOST': 'course-project-postgres',  #Server(伺服器)位址
        'PORT': '5432'  #PostgreSQL Port號
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
