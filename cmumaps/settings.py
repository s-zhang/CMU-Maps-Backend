"""
Django settings for cmumaps project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
<<<<<<< HEAD
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'rvyl0bzee7dv76=)0q5yvjjy^v7_1_d!8vo7q4(vdq0wap57u9'
=======
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vt8w+-rtsw=-lzldd$d&bw2q%*p6%!uwql!7f1ao%og7r_^z4o'
>>>>>>> eec08f3451ddcf2238afea3797acb2e94973fb11

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
<<<<<<< HEAD
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
=======
>>>>>>> eec08f3451ddcf2238afea3797acb2e94973fb11
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'cmumaps.urls'

WSGI_APPLICATION = 'cmumaps.wsgi.application'


# Database
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
=======
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
>>>>>>> eec08f3451ddcf2238afea3797acb2e94973fb11

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/topics/i18n/
=======
# https://docs.djangoproject.com/en/1.6/topics/i18n/
>>>>>>> eec08f3451ddcf2238afea3797acb2e94973fb11

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
<<<<<<< HEAD
# https://docs.djangoproject.com/en/1.7/howto/static-files/
=======
# https://docs.djangoproject.com/en/1.6/howto/static-files/
>>>>>>> eec08f3451ddcf2238afea3797acb2e94973fb11

STATIC_URL = '/static/'
