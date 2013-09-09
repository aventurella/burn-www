from burnlib.core.models import Model


class Workout(Model):

    def __init__(self):
        self.id = None
        self.label = None
        self.user = None
