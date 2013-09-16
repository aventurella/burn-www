from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User, GameCenterUser
from burnlib.workouts.models import Workout
from .base import SqlAlchemyTest


class TestWorkoutService(SqlAlchemyTest):

    def test_create_workout(self):
        users = self.ioc.UserService()
        workouts = self.ioc.WorkoutService()

        u1 = User()
        users.create_user(u1)

        w1 = Workout()
        w1.label = 'Test'
        w1.user = u1

        workouts.create_workout(w1)
        items = workouts.workouts_for_user(u1)

        self.assertTrue(len(items) == 1)
        self.assertTrue(items[0].id == w1.id)
        self.assertTrue(items[0].label == w1.label)

    def test_workout_for_id(self):
        users = self.ioc.UserService()
        workouts = self.ioc.WorkoutService()

        u1 = User()
        users.create_user(u1)

        w1 = Workout()
        w1.label = 'Test'
        w1.user = u1

        workouts.create_workout(w1)
        w2 = workouts.workout_for_id(w1.id)

        self.assertTrue(w2.id == w1.id)
        self.assertTrue(w2.label == w1.label)

    def test_workout_for_id_fail(self):

        workouts = self.ioc.WorkoutService()

        self.assertRaises(
            ResourceNotFound,
            workouts.workout_for_id,
            '999')

    def test_workouts_for_user(self):
        users = self.ioc.UserService()
        workouts = self.ioc.WorkoutService()

        u1 = User()
        users.create_user(u1)

        w1 = Workout()
        w1.label = 'Test3'
        w1.user = u1

        w2 = Workout()
        w2.label = 'Test1'
        w2.user = u1

        w3 = Workout()
        w3.label = 'Test2'
        w3.user = u1

        workouts.create_workout(w1)
        workouts.create_workout(w2)
        workouts.create_workout(w3)

        items = workouts.workouts_for_user(u1)

        self.assertTrue(len(items) == 3)
        self.assertTrue(items[0].id == w2.id)
        self.assertTrue(items[0].label == w2.label)

        self.assertTrue(items[1].id == w3.id)
        self.assertTrue(items[1].label == w3.label)

        self.assertTrue(items[2].id == w1.id)
        self.assertTrue(items[2].label == w1.label)

    def test_delete_workout(self):
        users = self.ioc.UserService()
        workouts = self.ioc.WorkoutService()

        u1 = User()
        users.create_user(u1)

        w1 = Workout()
        w1.label = 'Test'
        w1.user = u1

        workouts.create_workout(w1)
        workouts.workout_for_id(w1.id)

        workouts.delete_workout(w1)

        self.assertRaises(
            ResourceNotFound,
            workouts.workout_for_id,
            w1.id)

    def test_delete_user_cleanup(self):
        users = self.ioc.UserService()
        workouts = self.ioc.WorkoutService()

        u1 = User()
        users.create_user(u1)

        w1 = Workout()
        w1.label = 'Test'
        w1.user = u1

        workouts.create_workout(w1)
        workouts.workout_for_id(w1.id)

        users.delete_user(u1)

        self.assertRaises(
            ResourceNotFound,
            workouts.workout_for_id,
            w1.id)

    def test_add_workout_players(self):
        workouts = self.ioc.WorkoutService()
        gc_users = self.ioc.GameCenterUserService()

        u1 = GameCenterUser()
        u1.username = 'clarkonaut'
        u1.game_center_id = 'g:12345',
        u1.push_notification_token = 'abcdef'
        u1.user = User()

        u2 = GameCenterUser()
        u2.username = 'lucynaut'
        u2.game_center_id = 'g:54321',
        u2.push_notification_token = 'xyz'
        u2.user = User()

        u3 = GameCenterUser()
        u3.username = 'ollienaut'
        u3.game_center_id = 'g:67890',
        u3.push_notification_token = 'abxyz'
        u3.user = User()

        gc_users.create_user(u1)
        gc_users.create_user(u2)
        gc_users.create_user(u3)

        w1 = Workout()
        w1.label = 'Test'
        w1.user = u1.user

        w2 = Workout()
        w2.label = 'Test2'
        w2.user = u2.user

        workouts.create_workout(w1)
        workouts.create_workout(w2)

        w1.game_center_players.append(u2)
        w1.game_center_players.append(u3)

        w2.game_center_players.append(u1)
        w2.game_center_players.append(u3)

        w3 = workouts.workout_for_id(w1.id)
        players = w3.game_center_players

        self.assertTrue(len(players) == 2)
        self.assertTrue(players[0].username == u2.username)
        self.assertTrue(players[1].username == u3.username)

        w4 = workouts.workout_for_id(w2.id)
        players = w4.game_center_players

        self.assertTrue(len(players) == 2)
        self.assertTrue(players[0].username == u1.username)
        self.assertTrue(players[1].username == u3.username)

