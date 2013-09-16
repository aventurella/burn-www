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
        route_name='workouts.detail',
        request_method='PUT',
        renderer='json')
    def update_workout(self):
        # input:
        # {u'players': [u'G:1549014314']}
        # workout_id will be 'base' or an actual workout_id.
        # adding freinds to workout or "base" workout

        data = self.request.json_body
        log.debug('Received data %s', data)

        alias = self.request.matchdict['alias']
        workout_id = self.request.matchdict['workout_id']

        log.info('Updating workout \'%s\' for \'%s\' @ \'%s\'',
            workout_id, alias, data)

        if workout_id == 'base':
            pass

        return {'ok': True}

    @view_config(
        route_name='workouts.detail',
        request_method='GET',
        renderer='json')
    def get_workout(self):
        # input:
        # {u'players': [u'G:1549014314']}
        # workout_id will be 'base' or an actual workout_id.
        # adding freinds to workout or "base" workout

        data = self.request.json_body
        log.debug('Received data %s', data)

        alias = self.request.matchdict['alias']
        workout_id = self.request.matchdict['workout_id']

        log.info('Updating workout \'%s\' for \'%s\' @ \'%s\'',
            workout_id, alias, data)

        if workout_id == 'base':
            pass

        return {'ok': True}

    @view_config(
        route_name='workouts.begin',
        request_method='POST',
        renderer='json')
    def begin_workout(self):
        # input:
        # {u'start_date': u'2013-09-01T03:53:22.800Z', u'workout_id': u'1'}

        data = self.request.json_body
        log.debug('Received data %s', data)

        alias = self.request.matchdict['alias']
        workout_id = data['workout_id']

        log.info('Starting workout \'%s\' for \'%s\' @ \'%s\'',
            workout_id, alias, data['start_date'])

        return {'ok': True, 'data': {'id': 2}}

    @view_config(
        route_name='workouts.end',
        request_method='PUT',
        renderer='json')
    def end_workout(self):
        # input:
        # {u'end_date': u'2013-09-01T03:54:06.694Z'}

        data = self.request.json_body
        log.debug('Received data %s', data)

        alias = self.request.matchdict['alias']
        record_id = self.request.matchdict['record_id']

        log.info('Stopping workout \'%s\' for \'%s\' @ \'%s\'',
            record_id, alias, data['end_date'])

        return {'ok': True}
