from burnlib.core.models import Model


class User(Model):

    def __init__(self):
        self.id = None


class GameCenterUser(Model):
    def __init__(self):
        self.user = None
        self.game_center_id = None
        self.push_notification_token = None


