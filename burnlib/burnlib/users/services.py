from burnlib.core.services import Service


class GameCenterService(Service):
    def user_for_username(self, username):
        return self.driver.user_for_username(username)

    def user_for_id(self, user_id):
        return self.driver.user_for_id(user_id)

    def create_user(self, game_center_user):
        self.driver.create_user(game_center_user)


class UserService(Service):
    def create_user(self, user):
        self.driver.create_user(user)

    def user_for_id(self, user_id):
        return self.driver.user_for_id(user_id)
