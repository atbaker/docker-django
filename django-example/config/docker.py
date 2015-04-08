# -*- coding: utf-8 -*-
'''
Docker Sample Configuration

- Runs in Debug mode
- Uses console backend for emails
- Use Django Debug Toolbar
'''
from configurations import values
from .common import Common


class Docker(Common):

    # DEBUG
    DEBUG = values.BooleanValue(True)
    TEMPLATE_DEBUG = DEBUG
    # END DEBUG

    # INSTALLED_APPS
    INSTALLED_APPS = Common.INSTALLED_APPS
    # END INSTALLED_APPS

    # DATABASE CONFIGURATION

    # PORT_5432_TCP_ADDR = values.Value(environ_prefix='DB', environ_name='PORT_5432_TCP_ADDR')
    import os
    POSTGRES_HOST = os.environ['DB_PORT_5432_TCP_ADDR']
    DATABASES = values.DatabaseURLValue('postgres://postgres@{0}/postgres'.format(POSTGRES_HOST))
    # END DATABASE CONFIGURATION

    # Mail settings
    EMAIL_HOST = "localhost"
    EMAIL_PORT = 1025
    EMAIL_BACKEND = values.Value('django.core.mail.backends.console.EmailBackend')
    # End mail settings

    # django-debug-toolbar
    MIDDLEWARE_CLASSES = Common.MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar', 'gunicorn')

    # SITE CONFIGURATION
    # Hosts/domain names that are valid for this site
    # See https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
    ALLOWED_HOSTS = ["*"]
    # END SITE CONFIGURATION

    INTERNAL_IPS = ('127.0.0.1',)

    DEBUG_TOOLBAR_CONFIG = {
        'DISABLE_PANELS': [
            'debug_toolbar.panels.redirects.RedirectsPanel',
        ],
        'SHOW_TEMPLATE_CONTEXT': True,
    }
    # end django-debug-toolbar

    MEMCACHED_HOST = os.environ['CACHE_PORT_11211_TCP_ADDR']
    # CACHES = values.CacheURLValue(default="memcached://{0}:11211".format(MEMCACHED_HOST))
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
            'LOCATION': '{0}:11211'.format(MEMCACHED_HOST)
        }
    }

    # Your local stuff: Below this line define 3rd party libary settings