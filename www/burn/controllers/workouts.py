import logging
from .base import view_config
from .base import Controller


log = logging.getLogger(__name__)


class WorkoutsController(Controller):

    @view_config(
        route_name='workouts',
        request_method='GET',
        renderer='json')
    def workouts(self):
        alias = self.request.matchdict['alias']
        log.info('Retrieving workouts for \'%s\'', alias)

        return {'ok': True, 'data': [
            {'label': 'Backyard Workout', 'id': 1},
            {'label': 'Beach Workout', 'id': 2},
            {'label': 'Zombie Workout', 'id': 3},
            {'label': 'Drinking Beer Workout', 'id': 4},
            {'label': 'Being Fat Workout', 'id': 5}]
        }

    @view_config(
        route_name='workouts',
        request_method='POST',
        renderer='json')
    def create_workout(self):
        # input:
        # {u'label': u'New'}

        data = self.request.json_body
        alias = self.request.matchdict['alias']

        log.info('Creating workout \'%s\' for \'%s\'', data['label'], alias)
        log.debug('Received data %s', data)

        return {'ok': True, 'data': {'label': data['label'], 'id': 2}}

    @view_config(
        route_name='workouts.start',
        request_method='POST',
        renderer='json')
    def start_workout(self):
        # input:
        # {u'start_time': u'2013-08-16T03:15:30.600Z'}

        data = self.request.json_body
        alias = self.request.matchdict['alias']
        workout_id = self.request.matchdict['workout_id']

        log.info('Starting workout \'%s\' for \'%s\' @ \'%s\'',
            workout_id, alias, data['start_time'])
        log.debug('Received data %s', data)

        return {'ok': True}
