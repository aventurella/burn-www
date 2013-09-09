import logging
from sqlalchemy.orm import joinedload
from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import (User, GameCenterUser)
from .base import SqlAlchemyDriver

log = logging.getLogger(__name__)


class UserDriver(SqlAlchemyDriver):

    def create_user(self, user):
        session = self.session
        session.add(user)
        session.flush()

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


class GameCenterUserDriver(SqlAlchemyDriver):
    def user_for_username(self, username):
        session = self.session

        try:
            result = session.query(GameCenterUser)\
                            .options(joinedload(GameCenterUser.user)) \
                            .filter(GameCenterUser.username == username)\
                            .one()
        except Exception as e:
            exc = ResourceNotFound(GameCenterUser, e, username=username)
            log.warning(exc)
            raise exc

        return result

    def user_for_game_center_id(self, game_center_id):
        session = self.session

        try:
            result = session.query(GameCenterUser)\
                            .options(joinedload(GameCenterUser.user)) \
                            .filter(GameCenterUser.game_center_id == game_center_id)\
                            .one()
        except Exception as e:
            exc = ResourceNotFound(GameCenterUser, e, game_center_id=game_center_id)
            log.warning(exc)
            raise exc

        return result

    def create_user(self, game_center_user):
        session = self.session
        session.add(game_center_user)
        session.flush()

