class BurnlibException(Exception):
    def __init__(self, message=None):
        self.message = message
        super(BigMethodException, self).__init__()

    def __str__(self):
        if self.message:
            return self.message


class ResourceNotFound(BurnlibException):

    def __init__(self, kind, error, **kwargs):
        super(BurnlibException, self).__init__()
        self.qualname = '%s.%s' % (kind.__module__, kind.__name__)
        self.kind = kind
        self.params = kwargs
        self.error = error

    def __repr__(self):
        params = []

        if self.params:
            for k, v in self.params.iteritems():
                params.append('%s=%s' % (k, v))

        return '<%s(%s, %s) - %s>' % (
            self.__class__.__name__,
            self.kind.__name__,
            ', '.join(params),
            self.error.__class__.__name__)

    def __str__(self):
        message = 'Resource \'%s\' not found (%s: %s)' % (
            self.qualname,
            self.error.__class__.__name__,
            self.error)

        if self.params:
            params = []

            for k, v in self.params.iteritems():
                params.append('%s=%s' % (k, v))

            message = '%s for params %s' % (message, ' and '.join(params))

        return unicode(message)
