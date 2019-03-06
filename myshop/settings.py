"""
Django settings for myshop project.

Generated by 'django-admin startproject' using Django 2.0b1.

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
SECRET_KEY = 'w#c2p$9qpf@+%_f14c9g1%4lm*o0s2ht^*+4mx^77l($)l!1!6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
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

ROOT_URLCONF = 'myshop.urls'

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
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/etc/mysql/my.cnf',
        },
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_REDIRECT_URL = 'shop:product_list'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

CART_SESSION_ID = 'cart'


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Braintree settings
# BRAINTREE_MERCHANT_ID = 'wfp6x3vxdw2cw5pv'
# BRAINTREE_PUBLIC_KEY = '3d9jnwtcwrz7t3fr'
# BRAINTREE_PRIVATE_KEY = '6882859b5a089141b16e0e2bf9a8206b'

# from braintree import Configuration, Environment

# Configuration.configure(
#     Environment.Sandbox,
#     # Environment.Production,
#     BRAINTREE_MERCHANT_ID,
#     BRAINTREE_PUBLIC_KEY,
#     BRAINTREE_PRIVATE_KEY
# )

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# social
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    # 'account.authentication.EmailAuthBackend',
    # 'social_core.backends.facebook.FacebookOAuth2',
    # 'social_core.backends.twitter.TwitterOAuth',
    # 'social_core.backends.google.GoogleOAuth2',
]

# social auth settings
# SOCIAL_AUTH_FACEBOOK_KEY = '' # Facebook App ID
# SOCIAL_AUTH_FACEBOOK_SECRET = '' # Facebook App Secret
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
#
# SOCIAL_AUTH_TWITTER_KEY = '' # Twitter Consumer Key
# SOCIAL_AUTH_TWITTER_SECRET = '' # Twitter Consumer Secret
#
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '' # Google Consumer Key
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '' # Google Consumer Secret

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1
