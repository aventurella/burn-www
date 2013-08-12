import logging
from .base import view_config
from .base import Controller


log = logging.getLogger(__name__)


class WorkoutsController(Controller):

    @view_config(
        route_name='workouts',
        request_method='POST',
        renderer='json')
    def create_workout(self):
        # input:
        # {
        #  u'csrf_token': u'b5101730458fc89d817f3e6f8498702ae1e4efed',
        #  u'friends': [u'G:1549014314']
        # }

        data = self.request.json_body
        alias = self.request.matchdict['alias']

        log.info('Creating workout \'%s\' for \'%s\'', data['label'], alias)
        log.debug('Received data %s', data)

        #print(data['csrf_token'])
        #print(self.request.session.get_csrf_token())

        return {'ok': True, 'data': {'label': 'Workout Name', 'id': 1}}
