import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
PROJECT_DIR = os.path.join('..', os.path.dirname(BASE_DIR))

SECRET_KEY = ''

DEBUG = True

TEMPLATE_ROOT = os.path.join(BASE_DIR, 'apps', 'templates')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DOCS_URL = '/docs/'
DOCS_ROOT = os.path.join(BASE_DIR, 'docs')

SENTRY_DSN = ''
