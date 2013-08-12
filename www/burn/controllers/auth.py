import logging
from .base import view_config
from .base import Controller


log = logging.getLogger(__name__)


class AuthenticationController(Controller):

    @view_config(
        route_name='auth.gamecenter',
        request_method='POST',
        renderer='json')
    def gamecenter(self):

        # input:
        # print(self.request.json_body)
        # {
        #  u'player_id': u'G:1784131943',
        #  u'alias': u'aventurella',
        #  u'notification_token': u'f420...' # 63 chars
        # }

        data = self.request.json_body
        log.debug('Received data %s', data)
        log.info('Authenticating \'%s\' with Game Center Id \'%s\'',
            data['alias'],
            data['player_id'])

        token = self.request.session.get_csrf_token()
        return {'ok': True, 'data': {'token': token}}
