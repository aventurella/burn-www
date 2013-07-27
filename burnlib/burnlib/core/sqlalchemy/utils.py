from __future__ import absolute_import
from sqlalchemy.orm import relationship
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from burnlib.users.models import User
from burnlib.users.models import UserExtra

from .tables import (
    user, user_extra, metadata

)


def sqlalchemy_session_factory(config, **kwargs):
    engine = engine_from_config(config, **kwargs)
    return sessionmaker(bind=engine)


def sqlalchemy_scoped_session_factory(config):
    engine = engine_from_config(config)
    return scoped_session(sessionmaker(bind=engine))


def sqlalchemy_create_tables(params):
    engine = create_engine(params['sqlalchemy.url'], poolclass=NullPool)
    metadata.create_all(engine)


def sqlalchemy_map_models():
    '''
    Why classical mappings?

    Right now these models are backed by SQL, this may not be the case in the
    future. The models will probably remain unchanged, but their backing store
    may change as needs arise. In that case, we reap the benefits of SQLAlchemy
    without having making out models look like declarative base models.
    '''

    # http://docs.sqlalchemy.org/en/rel_0_8/orm/collections.html#passive-deletes
    mapper(User, user, properties={
        'extras': relationship(
            UserExtra,
            cascade='all, delete-orphan',
            passive_deletes=True,
            uselist=False,
            backref='user')
        })

    mapper(UserExtra, user_extra)
