import datetime
import random

from ft_api.domain.models import *
from ft_api.test.utils import *


class DataGenerator:

    @staticmethod
    def set_up_exercise(user=None, exercise_type=None):
        if not user:
            user = DataGenerator.set_up_user()
        if not exercise_type:
            exercise_type = DataGenerator.set_up_exercise_type()
        end_time = datetime.datetime.now()
        start_time = end_time - datetime.timedelta(hours=1)
        e = Exercise(user=user, exercise_type=exercise_type, start_time=start_time, end_time=end_time)
        e.save()
        return e

    @staticmethod
    def set_up_exercise_type(name=None, description=None, multiplier=None):
        if not name:
            name = generate_string(30)
        if not description:
            description = generate_string(30)
        if not multiplier:
            multiplier = random.randint(1, 100) / 100

        et = ExerciseType(name=name, description=description, multiplier=multiplier)
        et.save()
        return et

    @staticmethod
    def set_up_fitness_plan(user=None, fitness_plan_type=None, goal_weight=None):
        if not user:
            user = DataGenerator.set_up_user()
        if not fitness_plan_type:
            fitness_plan_type = DataGenerator.set_up_fitness_plan_type()

        fp = FitnessPlan(user=user, fitness_plan_type=fitness_plan_type, goal_weight=goal_weight)
        fp.save()
        return fp

    @staticmethod
    def set_up_fitness_plan_type(name=None, description=None, pounds_per_week=None):
        if not name:
            name = generate_string(30)
        if not description:
            description = generate_string(30)
        if not pounds_per_week:
            pounds_per_week = random.randint(1, 100) / 100

        fpt = FitnessPlanType(name=name, description=description, pounds_per_week=pounds_per_week)
        fpt.save()
        return fpt

    @staticmethod
    def set_up_user(username=None, first_name=None):
        if not username:
            username = generate_email_address()
        if not first_name:
            first_name = generate_id(10)

        user = User(username=username, password=generate_id(10), first_name=first_name, last_name=generate_id(10))
        user.save()
        return user


class MockRequestsResponse:
    def __init__(self, status_code=None, text=None, mock_json=None):
        self.status_code = status_code
        self.text = text
        self.mock_json = mock_json

    def json(self):
        return self.mock_json
