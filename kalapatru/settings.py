"""
Django settings for kalapatru project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import dj_database_url
from os.path import join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ROOT = os.path.abspath(os.path.dirname(__name__))
print SITE_ROOT
try:
    from dotenv import load_dotenv
    dotenv_path=join(SITE_ROOT,'.env')
    load_dotenv(dotenv_path)
except Exception,e:
    print e
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j%geyfdcwn@d70hv@znz=lw7nx6vyr*6#sgfq_2%6$i!*k=+41'

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
    'LR',
    'corsheaders',
    'model_report',
    'app',
    'stock',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

ROOT_URLCONF = 'kalapatru.urls'

WSGI_APPLICATION = 'kalapatru.wsgi.application'
DATABASES_URL = 'mysql://root:root@localhost:3306/kalptaru1'
DATABASES =  {'default': dj_database_url.parse(os.environ.get('DATABASES_URL',DATABASES_URL))}
print os.environ.get('DATABASES_URL','------------------')

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
from os.path import abspath, dirname, basename, join
import sys

PROJECT_ABSOLUTE_DIR = dirname(abspath(__file__))
PROJECT_NAME = basename(PROJECT_ABSOLUTE_DIR)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "templates"),
)


# TEMPLATE_DIRS = [(SITE_ROOT+'/templates')]
print ">>>>>>>>>>>>>>>>>>>>>>>>",TEMPLATE_DIRS
MEDIA_ROOT = PROJECT_ABSOLUTE_DIR + '/media/'

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = PROJECT_ABSOLUTE_DIR + '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/usr/local/lib/python2.7/dist-packages/django/contrib/admin/static/',
)

if os.environ.get('PRODUCTION', None):
    from LR.prodSettings import DATABASES as prodDB
    STATIC_ROOT ='/usr/local/lib/python2.7/dist-packages/django/contrib/admin/'





STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'
DEBUG=True
