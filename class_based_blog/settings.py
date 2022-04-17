"""
Django settings for class_based_blog project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import django_heroku

# from dotenv import dotenv_values
# config=dotenv_values('.env')
from dotenv import load_dotenv
load_dotenv()  

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9loge=s56xpk(wc*dskit1ki$smn+x!ean3i#ow+)ajgk35t8j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'home',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   
    'django.contrib.humanize',
    'crispy_forms',
    'rest_framework',
    'rest_framework.authtoken'#for token authentication,
]
CRISPY_TEMPLATE_PACK = 'bootstrap4'#For Crispy
#Restframework Authentication
REST_FRAMEWORK = {
    #For authentication
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    #For permission
    'DEFAULT_PERMISSION_CLASSES': [
        
        'rest_framework.permissions.IsAuthenticated',
    ],
    #For pagination
    'DEFAULT_PAGINATION_CLASSE': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE':1,#only one show in one page
    
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#for heroku
]

ROOT_URLCONF = 'class_based_blog.urls'

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

WSGI_APPLICATION = 'class_based_blog.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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
AUTH_USER_MODEL='home.User'
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_STORAGE=['whitenoise.storage.CompressedManifestStaticFilesStorage']
# STATIC_URL = '/static/'


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# after logout and login it redirects to root /
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
#EmailS Sender
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = config['EMAIL_HOST_USER']
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')

# EMAIL_HOST_PASSWORD = config['EMAIL_HOST_PASSWORD']
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
#Configuring media 
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # 'media' is my media folder
MEDIA_URL = '/media/'
#Activating Heroku
django_heroku.settings(locals())
#Ecommerce Secret Key-> django-insecure-nw93-^vr_5@8047+b%peuy_$#5b%5h*b38_a1rkc+((m3r3#q+