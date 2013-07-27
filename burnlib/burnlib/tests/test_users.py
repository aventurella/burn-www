import unittest
from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, UserExtra
#from .ioc import build_container


class TestUserService(unittest.TestCase):

    def setUp(self):
        #self.ioc = build_container()
        pass

    def test_create_user(self):
        extras = UserExtra()
        extras.blitz_id = 'afde4b5c'

        u1 = User()
        u1.username = 'lucy'
        u1.extras = extras

        users = self.ioc.UserService()
        users.create_user(u1)

        self.addCleanup(users.delete_user, u1)

        self.assertTrue(u1.id != None)
        self.assertTrue(u1.extras.id != None)
