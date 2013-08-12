from .base import view_config
from .base import Controller


class FriendsController(Controller):

    @view_config(
        route_name='friends.register',
        request_method='POST',
        renderer='json')
    def register(self):
        # input:
        # print(self.request.json_body)
        # {
        #  u'csrf_token': u'b5101730458fc89d817f3e6f8498702ae1e4efed',
        #  u'friends': [u'G:1549014314']
        # }

        data = self.request.json_body
        alias = self.request.matchdict['alias']

        print(data['csrf_token'])
        print(self.request.session.get_csrf_token())

        return {'ok': True}
