from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, GameCenterUser
from .base import SqlAlchemyTest


class TestUserService(SqlAlchemyTest):

    def test_create_user(self):
        gc_user = GameCenterUser()
        extras.blitz_id = 'afde4b5c'

        u1 = User()
        u1.username = 'lucy'
        u1.extras = extras

        users = self.ioc.UserService()
        users.create_user(u1)

        self.addCleanup(users.delete_user, u1)

        self.assertTrue(u1.id != None)
        self.assertTrue(u1.extras.id != None)
