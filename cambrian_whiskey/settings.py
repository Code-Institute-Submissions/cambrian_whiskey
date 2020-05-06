"""
Django settings for cambrian_whiskey project.

Generated by 'django-admin startproject' using Django 1.11.28.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# so to actually use our env.py variables, we have to put import env at the top of the settings.py file. That will import our entire file and let us access to our environment variables

# removing the import env below as we are running everything through Heroku
import env
# import dj_database_url

# if os.path.exists('env.py'):
    # import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'cambrian-whiskey.herokuapp.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_forms_bootstrap',
    'accounts',
    'products',
    'cart',
    'checkout',
    'storages',
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

ROOT_URLCONF = 'cambrian_whiskey.urls'

# all directories named 'templates' potentially contain templates therefore we must set the DIRS TEMPLATES setting below to allow this. This way we can set each template for each application

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
                'django.template.context_processors.media',
                'cart.contexts.cart_contents',
            ],
        },
    },
]

# context_processors are lists of things that are available on every webpage

WSGI_APPLICATION = 'cambrian_whiskey.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases


# 'DATABSE_URL' originates from heroku/settings/configVars

if 'DATABASE_URL' in os.environ:
    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}
else:
    print('Databse URL not found. Using SQlite instead')
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }



# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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

# BY DOING THE FOLLOWING I SHOULD HAVE LOGIN CAPABILITY

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend', 'accounts.backends.CaseInsensitiveAuth'
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

# Then we can make some changes to our settings.py in order to connect to AWS. Static files tend not to change that many things, like CSS, so browsers will often cache them.So the first thing that we're going to add in here is just something to allow boto to know that it can cache the static files.

# PRODUCTION CONFIGURATION


# AWS_S3_OBJECT_PARAMETERS = {
#     'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#     'CacheControl': 'max-age=94608000',
# }

# AWS_STORAGE_BUCKET_NAME = 'cambrian-whiskey'
# AWS_S3_REGION_NAME = 'eu-west-2'
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# cambrian-whiskey.s3.amazonaws.com

# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'

# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATICFILES_STORAGE = 'custom_storages.StaticStorage'

STATIC_URL = '/static/'
# any directory called 'static' CAN contain staticfiles
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# our MEDIAFILES_LOCATION will be media, so any directory called media
MEDIAFILES_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'

# the following MESSAGE_STORAGE is to fix an issue we have with cloud 9. but im not on cloud 9 so i will uncomment

# MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorahe'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

MEDIA_URL = '/media/'

# CODE INSTITUTE found an issue in a video so instead of :MEDIA_URL = '/media/' they tell us to input the following:

# MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# OS MEANS WHATEVER COMPUTER THIS IS RUNNING ON. AND IN THIS CASE ITS WINDOWS. GET AN ENVIRONMENT VARIABLE AND WE ARE GOING TO CREATE AN ENVIRNMENT VARIABLE CALLED 'STRIPE_PUBLISHABLE' AND 'STRIPE_SECRET'. THIS IS SO THAT THE USERS CANNOT SEE THE KEYS PARTICULARLY THE SECRET KEYS OTHERWISE THEY ARE ABLE TO 'hack' INTO OUR ACCOUNT
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')
STRIPE_SECRET = os.getenv('STRIPE_SECRET')




