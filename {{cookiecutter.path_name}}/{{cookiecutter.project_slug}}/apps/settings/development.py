import os

from .base import *

SQL_ECHO = False

DATABASES = {
    'default': {
        'ENGINE': 'mssql+pymssql',
        'HOST': 's500devsql01.magazineluiza.intranet',
        'NAME': 'dbmagazine_xp',
        'USER': 'devfcamara',
        'PASSWORD': 'DEVFCAMARA',
        'PORT': 1433
    }
}

