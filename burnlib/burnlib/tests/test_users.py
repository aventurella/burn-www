from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, GameCenterUser
from .base import SqlAlchemyTest


class TestUserService(SqlAlchemyTest):

    def test_create_user(self):
        users = self.ioc.UserService()
        u1 = User()
        users.create_user(u1)

        self.assertTrue(u1.id != None)

    def test_user_for_id(self):
        users = self.ioc.UserService()
        u1 = User()
        users.create_user(u1)

        u2 = users.user_for_id(u1.id)
        self.assertTrue(u1.id == u2.id)

    def test_user_for_id_fail(self):
        users = self.ioc.UserService()

        self.assertRaises(
            ResourceNotFound,
            users.user_for_id,
            '999')

    def test_delete_user(self):
        users = self.ioc.UserService()

        u1 = User()
        users.create_user(u1)

        # just want to make sure it's not a resource error
        users.user_for_id(u1.id)

        users.delete_user(u1)

        self.assertRaises(
            ResourceNotFound,
            users.user_for_id,
            u1.id)


class TestGameCenterUserService(SqlAlchemyTest):

    def test_create_user(self):
        users = self.ioc.GameCenterUserService()

        u1 = GameCenterUser()
        u1.username = 'clarkonaut'
        u1.game_center_id = 'g:12345',
        u1.push_notification_token = 'abcdef'
        u1.user = User()

        users.create_user(u1)

        self.assertTrue(u1.id != None)
        self.assertTrue(u1.user.id != None)

    def test_user_for_game_center_id(self):
        users = self.ioc.GameCenterUserService()

        u1 = GameCenterUser()
        u1.username = 'clarkonaut'
        u1.game_center_id = 'g:12345',
        u1.push_notification_token = 'abcdef'
        u1.user = User()

        users.create_user(u1)

        u2 = users.user_for_game_center_id(u1.game_center_id)
        self.assertTrue(u1.game_center_id == u2.game_center_id)

    def test_user_for_game_center_id_fail(self):
        users = self.ioc.GameCenterUserService()

        self.assertRaises(
            ResourceNotFound,
            users.user_for_game_center_id,
            '999')

    def test_user_for_username(self):
        users = self.ioc.GameCenterUserService()

        u1 = GameCenterUser()
        u1.username = 'clarkonaut'
        u1.game_center_id = 'g:12345',
        u1.push_notification_token = 'abcdef'
        u1.user = User()

        users.create_user(u1)

        u2 = users.user_for_username(u1.username)
        self.assertTrue(u1.username == u2.username)

    def test_user_for_username_fail(self):
        users = self.ioc.GameCenterUserService()

        self.assertRaises(
            ResourceNotFound,
            users.user_for_username,
            '999')

    def test_delete_user_cleanup(self):
        users = self.ioc.UserService()
        gc_users = self.ioc.GameCenterUserService()

        u1 = GameCenterUser()
        u1.username = 'clarkonaut'
        u1.game_center_id = 'g:12345',
        u1.push_notification_token = 'abcdef'
        u1.user = User()

        gc_users.create_user(u1)

        u2 = users.user_for_id(u1.user.id)
        users.delete_user(u2)

        self.assertRaises(
            ResourceNotFound,
            gc_users.user_for_game_center_id,
            u1.game_center_id)

    # def test_register_freinds(self):
    #     gc_users = self.ioc.GameCenterUserService()

    #     u1 = GameCenterUser()
    #     u1.username = 'clarkonaut'
    #     u1.game_center_id = 'g:12345',
    #     u1.push_notification_token = 'abcdef'
    #     u1.user = User()

    #     gc_users.create_user(u1)

    #     u1.freinds =
    #     # G:1549014314
