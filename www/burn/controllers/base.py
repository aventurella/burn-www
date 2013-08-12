from pyramid.view import view_config


class Controller(object):
    def __init__(self, request):
        self.request = request


