from burnlib.core.services import Service


class WorkoutService(Service):
    def workouts_for_user(self, user):
        return self.driver.workouts_for_user(user)

    def workout_for_id(self, workout_id):
        return self.driver.workout_for_id(workout_id)

    def create_workout(self, workout):
        self.driver.create_workout(workout)

    def update_workout(self, workout):
        self.driver.update_workout(workout)

    def delete_workout(self, workout):
        self.driver.delete_workout(workout)
