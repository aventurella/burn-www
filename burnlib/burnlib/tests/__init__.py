from burnlib.core.configuration import settings
from burnlib.sqlalchemy.utils import sqlalchemy_map_models
from burnlib.sqlalchemy.utils import sqlalchemy_create_tables
from burnlib.sqlalchemy.tables import metadata


def setUpPackage():
    sqlalchemy_map_models()
    sqlalchemy_create_tables(
        settings.data['burn:sqlalchemy:test'],
        metadata)


def tearDownPackage():
    pass
