from burnlib.users.models import (User, GameCenterUser)
from .base import SqlAlchemyDriver


class UserDriver(SqlAlchemyDriver):
    def create_user(self, user):
        pass

    def user_for_id(self, user_id):
        return User()


class GameCenterDriver(SqlAlchemyDriver):
    def user_for_username(self, username):
        return GameCenterUser()

    def user_for_id(self, user_id):
        return GameCenterUser()

    def create_user(self, game_center_user):
        pass

