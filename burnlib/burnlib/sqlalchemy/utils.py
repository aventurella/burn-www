from __future__ import absolute_import
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapper
from sqlalchemy import create_engine
from sqlalchemy import engine_from_config
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from burnlib.users.models import User
from burnlib.users.models import GameCenterUser
from .tables import (
    user, game_center_user
)


def sqlalchemy_session_factory(config, **kwargs):
    engine = engine_from_config(config, **kwargs)
    return sessionmaker(bind=engine)


def sqlalchemy_create_tables(params, metadata):
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

    mapper(GameCenterUser, game_center_user, properties={
        'user': relationship(
            User,
            cascade='all, delete-orphan',
            passive_deletes=True,
            uselist=False,
            backref='game_center')
        })

    mapper(User, user)
