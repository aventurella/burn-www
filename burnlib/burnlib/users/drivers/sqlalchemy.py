from __future__ import absolute_import
import logging
from sqlalchemy.orm import joinedload, contains_eager
from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, GameCenterUser
from burnlib.sqlalchemy.drivers.base import SqlAlchemyDriver


log = logging.getLogger(__name__)


class SqlAlchemyUserDriver(SqlAlchemyDriver):

    def create_user(self, user):
        session = self.session
        session.add(user)

    def delete_user(self, user):
        log.info('Deleting user with id %s', user.id)
        session = self.session
        session.delete(user)

    def user_for_id(self, user_id):
        session = self.session

        try:
            result = session.query(User).filter(User.id == user_id).one()
        except Exception as e:
            exc = ResourceNotFound(User, e, id=user_id)
            log.warning(exc)
            raise exc

        return result

    # def user_for_game_center_id(self, game_center_id):
    #     session = self.session(expire_on_commit=False)
    #     result = None

    #     try:
    #         result = session.query(User) \
    #                 .options(joinedload(User.extras),
    #                          contains_eager('extras.user')) \
    #                 .join(UserExtra) \
    #                 .filter(UserExtra.game_center_id == game_center_id) \
    #                 .one()
    #     except Exception as e:
    #         exc = ResourceNotFound(User, e, game_center_id=game_center_id)
    #         log.warning(exc)
    #         raise exc

    #     session.close()
    #     return result
