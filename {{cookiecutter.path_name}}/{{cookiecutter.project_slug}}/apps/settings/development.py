import os

from .base import *

SQL_ECHO = True

DATABASES = {
    'default': {
        'ENGINE': 'sqlite',
        'HOST': '',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': '',
        'PASSWORD': '',
        'PORT': ''
    }
}

