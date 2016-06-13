# set env
import os
os.environ.setdefault('SIMPLE_SETTINGS', 'apps.settings.test')

import pytest
from app import make_app

from contrib.db import session as db_session
from contrib.db import Model

from mixer.backend.sqlalchemy import Mixer


@pytest.fixture
def app(request):
    return make_app()


@pytest.fixture(scope='module')
def db(request):
    Model.create_all()

    def teardown():
        Model.drop_all()

    request.addfinalizer(teardown)


@pytest.fixture(scope='session')
def session():
    return db_session


@pytest.fixture
def mixer(session):
    return Mixer(session=session)
