def includeme(config):
    config.add_route('auth.gamecenter', '/authenticate/gamecenter')
    config.add_route('friends.register', '/{alias}/friends')
    config.add_route('workouts', '/{alias}/workouts')
    config.add_route('workouts.start', '/{alias}/workouts/{workout_id}')


    # config.add_route('home', '/')
    # #config.add_route('login', '/login')
    # config.add_route('logout', '/logout')
    # config.add_route('blitz_login', '/login/blitz')


    # config.add_route('channel.finalize', '/channels/{channel_id:com.(?:[a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]+}/{client_id:[a-z][a-z0-9-]+}/{account_id:[a-f0-9]{32}}')
    # config.add_route('channel.authorize', '/channels/{channel_id:com.(?:[a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]+}/{client_id:[a-z][a-z0-9-]+}/authorize')

    # config.add_route('channel.callback', '/channels/callback')
    # #config.add_route('channel.callback', '/services/callback/facebook')

    # config.add_route('clients', '/clients')
    # config.add_route('clients.detail', '/clients/{client_id:[a-zA-Z0-9][a-zA-Z0-9\-]+}')
    # # config.include('bigview.urls')
