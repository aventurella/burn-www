from burnlib.core.exceptions import ResourceNotFound
from burnlib.users.models import User
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
