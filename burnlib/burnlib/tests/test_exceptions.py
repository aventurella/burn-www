import io
import unittest
import logging
from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User


class TestBurnlibExceptions(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(format='%(message)s')
        self.buffer = io.BytesIO()
        self.logger = logging.getLogger('log_test')
        self.logger.setLevel(logging.DEBUG)

        # If we were emitting unicode from our log handler  in python 2 we can
        # use the io.StringIO buffer which is backported from 3x. If we
        # were using the StreamHandler in 2x we would need to change the
        # buffer to io.BytesIO
        handler = logging.StreamHandler(self.buffer)

        self.logger.addHandler(handler)

    def test_resource_not_found_str(self):
        x = Exception()
        exc = ResourceNotFound(User, x, id=1)
        self.assertTrue(
            str(exc) == \
            "Resource 'burnlib.users.models.User' not found (Exception: ) for params id=1")

    def test_resource_not_found_log(self):
        x = Exception()
        exc = ResourceNotFound(User, x, id=1)
        self.logger.warning(exc)

        data = self.buffer.getvalue()
        self.assertTrue(data.strip() == \
            "Resource 'burnlib.users.models.User' not found (Exception: ) for params id=1")
