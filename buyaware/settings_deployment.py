from settings import *
DEBUG = False
TEMPLATE_DEBUG = DEBUG

FORCE_SCRIPT_NAME = ''

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'buyaware_buyaware',
        'USER': 'buyaware',
        'PASSWORD': 'Admin@BuyAware4Life!',
        'HOST': '',
        'PORT': '',
    }
   }
