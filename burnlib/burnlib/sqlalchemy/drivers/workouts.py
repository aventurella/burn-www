import logging
from burnlib.core.exceptions import ResourceNotFound
from burnlib.workouts.models import Workout
from .base import SqlAlchemyDriver

log = logging.getLogger(__name__)


class WorkoutDriver(SqlAlchemyDriver):
    def workouts_for_user(self, user):
        session = self.session
        results = session.query(Workout) \
                         .filter(Workout.user_id == user.id) \
                         .order_by(Workout.label.asc()) \
                         .all()

        return results

    def create_workout(self, workout):
        session = self.session
        session.add(workout)
        session.flush()

    def workout_for_id(self, workout_id):
        session = self.session

        try:
            result = session.query(Workout) \
                            .filter(Workout.id == workout_id) \
                            .one()
        except Exception as e:
            exc = ResourceNotFound(Workout, e, id=workout_id)
            log.warning(exc)
            raise exc

        return result

    def delete_workout(self, workout):
        log.info('Deleting workout with id %s', workout.id)
        session = self.session
        session.delete(workout)
