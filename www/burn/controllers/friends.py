import logging
from .base import view_config
from .base import Controller


log = logging.getLogger(__name__)


class FriendsController(Controller):

    @view_config(
        route_name='friends.register',
        request_method='POST',
        renderer='json')
    def register(self):
        # input:
        # {u'friends': [u'G:1549014314']}

        data = self.request.json_body
        alias = self.request.matchdict['alias']

        log.info('Registered friends \'%s\' for \'%s\'', data['friends'], alias)
        log.debug('Received data %s', data)

        # user.friends = {
        #     'G:1549014314': None
        # }

        return {'ok': True}
