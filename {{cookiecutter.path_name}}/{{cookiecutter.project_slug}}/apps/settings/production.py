from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'sqlite3',
        'HOST': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': ''
        'USER': '',
        'PASSWORD': ''
        'PORT': ''
    }
}
