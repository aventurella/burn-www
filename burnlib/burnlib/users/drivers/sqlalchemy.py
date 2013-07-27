from __future__ import absolute_import
import logging
from sqlalchemy.orm import joinedload, contains_eager
from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, UserExtra
from burnlib.core.sqlalchemy.drivers import SqlAlchemyDriver


log = logging.getLogger(__name__)


class SqlAlchemyUserDriver(SqlAlchemyDriver):

    def update_user(self, user):
        self.create_user(user)

    def create_user(self, user):
        session = self.session(expire_on_commit=False)

        if user.extras is None:
            user.extras = UserExtra()

        session.add(user)

        try:
            session.commit()
        except Exception as exc:
            log.warning(exc)
            pass

        session.close()

    def delete_user(self, user):
        log.info('Deleting user with id %s', user.id)
        session = self.session(expire_on_commit=False)
        session.delete(user)

        try:
            session.commit()
        except Exception as exc:
            log.warning(exc)
            pass

        session.close()

    def user_for_id(self, user_id):
        session = self.session(expire_on_commit=False)

        try:
            result = session.query(User) \
                    .options(joinedload(User.extras),
                             contains_eager('extras.user')) \
                    .filter(User.id == user_id) \
                    .one()
        except Exception as e:
            exc = ResourceNotFound(User, e, id=user_id)
            log.warning(exc)
            raise exc

        session.close()
        return result

    def user_for_game_center_id(self, game_center_id):
        session = self.session(expire_on_commit=False)
        result = None

        try:
            result = session.query(User) \
                    .options(joinedload(User.extras),
                             contains_eager('extras.user')) \
                    .join(UserExtra) \
                    .filter(UserExtra.game_center_id == game_center_id) \
                    .one()
        except Exception as e:
            exc = ResourceNotFound(User, e, game_center_id=game_center_id)
            log.warning(exc)
            raise exc

        session.close()
        return result
