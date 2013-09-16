from burnlib.core.models import Model


class Workout(Model):

    def __init__(self):
        self.id = None
        self.label = None
        self.user = None
        self.game_center_players = []


class WorkoutPlayer(Model):
    def __init__(self, game_center_player=None, workout=None):
        self.game_center_player = game_center_player
        self.workout = workout
