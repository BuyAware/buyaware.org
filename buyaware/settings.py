# -*- coding: utf-8 -*-
# Django settings for buyaware project.

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket

# For localization 
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sq!-60v-8k59waqol&amp;!ws6o*$h5&amp;2dlincqxeym3fuw_8d00k$'

ALLOWED_HOSTS = [
    '.buyaware.org',
]

SITE_ID = 1

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEST_RUNNER = 'django.test.runner.DiscoverRunner'

SERVER_EMAIL = 'info@wservices.ch'
DEFAULT_FROM_EMAIL = 'eric.mhr.brunner@gmail.com'

ADMINS = (
    (u'Eric Brunner', 'eric.mhr.brunner@gmail.com'),
)

MANAGERS = ADMINS


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': 'mydatabase',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Absolute path to the directory that holds media.
# Example: "/home/username/projectname/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# The absolute path to the directory where collectstatic will collect static files for deployment.
# Example: "/home/username/projectname/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# URL to use when referring to static files located in STATIC_ROOT.
# Examples: "/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# For static assets that arent't tied to a particular app. 
# In addition to using a static/ directory inside your apps, you can define a list of directories 
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'common_static'),
)

INSTALLED_APPS = (
    'home.apps.HomeConfig',
    'blog',
    'about',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    ### IMPORTED PROJECTS ###
    'modeltranslation',   # translate model data in registered languages
    'tinymce',   # WYSIWIG richtext editor
    'photologue',   # Picture management tool and toolbox
    'sortedm2m',   # custom many2many relationship which remembers order

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            ],
        },
    },
]


ROOT_URLCONF = 'buyaware.urls'

WSGI_APPLICATION = 'buyaware.wsgi.application'

# Override the server-derived value of SCRIPT_NAME 
# See http://code.djangoproject.com/wiki/BackwardsIncompatibleChanges#lighttpdfastcgiandothers
FORCE_SCRIPT_NAME = ''

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#Languages in which the web page is translated
LANGUAGES = (
    ('en', _('English')),
    ('de', _('Deutsch')),
    ('fr', _('Francais')),
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


# <----- BLOG SETTINGS -----> 

POSTS_PER_PAGE = 5


# <----- TINYMCE SETTINGS -----> 

TINYMCE_JS_URL = STATIC_URL + 'js/tinymce/tinymce.min.js'
TINYMCE_JS_ROOT = STATIC_ROOT + 'js/tinymce'
TINYMCE_DEFAULT_CONFIG = {
    #'toolbar': ,
    'plugins': "table,spellchecker,paste,searchreplace, image imagetools",
    'theme': "modern",
    'imagetools_cors_hosts': ['buyaware.org'],
}
TINYMCE_SPELLCHECKER = True
