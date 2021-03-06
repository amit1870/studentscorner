"""
Django settings for studentscorner project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%%*v@1w-)z-)8#32)_x%n)4ll!@nq_@o*+0-nzthgej^fw^s-0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ENABLE_SSL = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'accounts',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'catalog',
    'utils',
    'cart',
    'checkout',
    
    # 'djangodblog',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    # 'studentscorner.SSLMiddleware.SSLRedirect'
    # 'djangodblog.DBLogMiddleware',
]

ROOT_URLCONF = 'studentscorner.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'utils.context_processors.studentscorner',
            ],
        },
    },
]

WSGI_APPLICATION = 'studentscorner.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'studentstore',
        'USER': 'amit',
        'PASSWORD': 'n0wL!nux',
        'HOST': '',
        'PORT': '',
    }
}


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SESSION_COOKIE_AGE = 60 * 60 * 24 * 90

# for checkout 
GOOGLE_CHECKOUT_MERCHANT_ID = 'your id here'

GOOGLE_CHECKOUT_MERCHANT_KEY = 'your key here'

GOOGLE_CHECKOUT_URL = 'https://sandbox.google.com/checkout/api/v2/merchantCheckout/Merchant/' + GOOGLE_CHECKOUT_MERCHANT_ID

AUTHNET_POST_URL = 'test.authorize.net'

AUTHNET_POST_PATH = '/gateway/transact.dll'

AUTHNET_LOGIN = '9zWKbhaT75q'

AUTHNET_KEY = '2b28P4r3Vj9A76SK'

LOGIN_REDIRECT_URL = '/accounts/my_account/'

AUTH_PROFILE_MODULE = 'accounts.userprofile'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/


STATIC_URL = '/static/'

SITE_NAME = 'Students Corner'

SITE_ID = 1

META_KEYWORDS = 'Food, Fruits'

META_DESCRIPTION = 'This is for desc'
