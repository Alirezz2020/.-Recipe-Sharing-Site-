"""
Django settings for CallProject project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Media files settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hq=*)cv#nzhl3t!6_2x)+y9$h&)xpqv1e6ezd)9+k8wod#2q^+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home.apps.HomeConfig',
    'accounts.apps.AccountsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recipe_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'recipe_project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True




DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# for sending email (forget password part) you need to provide a service to send emails
# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Or other backend (e.g., console, filebased)
EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server hostname (e.g., for Gmail)
EMAIL_PORT = 587  # Your SMTP server port (e.g., 587 for Gmail with TLS)
EMAIL_USE_TLS = True  # Whether to use TLS (recommended)
EMAIL_HOST_USER = 'your_email@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'your_email_password'  # Your email password or app password (see explanation below)
DEFAULT_FROM_EMAIL = 'your_email@gmail.com' # The default sender email address for Django's emails


"""Explanation of Email Settings:

EMAIL_BACKEND: Specifies the email backend to use.  django.core.mail.backends.smtp.EmailBackend is the standard backend for sending emails via an SMTP server.  Other backends exist (e.g., for testing: django.core.mail.backends.console.EmailBackend prints emails to the console, django.core.mail.backends.filebased.EmailBackend saves emails to files).

EMAIL_HOST: The hostname of your SMTP server.  For Gmail, it's smtp.gmail.com.  For other providers, consult their documentation.

EMAIL_PORT: The port number for your SMTP server.  Common ports are 587 (for TLS) and 465 (for SSL). Gmail typically uses 587 with TLS.

EMAIL_USE_TLS: A boolean indicating whether to use Transport Layer Security (TLS).  TLS is highly recommended for secure email transmission. Set this to True.

EMAIL_HOST_USER: Your email address that will be used to authenticate with the SMTP server.

EMAIL_HOST_PASSWORD:  Important Security Note:  Do not directly use your regular email password here.  This is a significant security risk.  Instead, you should generate an "app password" specifically for Django (or any other application).

Gmail App Passwords: Go to your Google Account settings, then Security, and look for "App passwords". Create a new app password for your Django project. Use this app password as the value for EMAIL_HOST_PASSWORD.
Other Email Providers: Most providers have similar mechanisms for generating app-specific passwords or API keys. Consult their documentation.
DEFAULT_FROM_EMAIL: The default "From" email address that will be used when sending emails from your Django application.  It's good practice to set this to a valid email address."""


# ... other settings ...