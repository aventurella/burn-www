import logging
from .base import view_config
from .base import Controller


log = logging.getLogger(__name__)


class HomeController(Controller):

    @view_config(route_name='home')
    def authorize(self, channel_id, client_id):
        channels = self.ioc.ChannelService()
        channel = channels.channel_for_id(channel_id)

        plugin = load_plugin(
            channel.auth_handler,
            invoke_on_load=True,
            invoke_kwargs={
            'client_id': channel.oauth_client_key,
            'client_secret': channel.oauth_client_secret})

        session = SessionManager.from_clean(
            self.request.session, ChannelAuthorizationSession)

        session.data.client_id = client_id
        session.data.channel_id = channel_id

        redirect_uri = self.request.route_url('channel.callback')

        data = plugin.obj.plugin_authorize(
            redirect_uri=redirect_uri,
            remember=session.data.plugin_data)

        session.flush()
        return self.redirect(data)
