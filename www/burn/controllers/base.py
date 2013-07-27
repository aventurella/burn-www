from pyramid.view import view_config
#from pyramid_viewresult import Controller as ViewResultController


#class Controller(ViewResultController):
class Controller(object):
    def __init__(self, request):
        super(Controller, self).__init__(request)
        settings = request.registry.settings
        self.ioc = settings['ioc']

