from bigmethod.core.services import Service


class UserService(Service):
    def create_user(self, user):
        self.driver.create_user(user)

    def delete_user(self, user):
        self.driver.delete_user(user)

    def update_user(self, user):
        self.driver.update_user(user)

    def user_for_id(self, user_id):
        return self.driver.user_for_id(user_id)

    def user_for_game_center_id(self, game_center_id):
        return self.driver.user_for_game_center_id(game_center_id)
