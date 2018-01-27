import datetime

from django.db import models
from django.utils import timezone

from rest_framework_simplify.models import SimplifyModel


class ApiEndpoint(SimplifyModel):
    id = models.AutoField(primary_key=True)
    endpoint = models.CharField(max_length=150, null=False, blank=False)

    class Meta:
        db_table = 'api_endpoint'


class ApiKey(SimplifyModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    access_key = models.CharField(max_length=128)
    secret_access_key = models.CharField(max_length=128)
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=False, default=timezone.now)

    class Meta:
        db_table = 'api_key'


class ApiPermission(SimplifyModel):
    id = models.AutoField(primary_key=True)
    api_key = models.ForeignKey('Application', null=False, related_name='application')
    api_endpoint = models.ForeignKey('ApiEndpoint', null=False, related_name='api_permissions')
    methods = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        db_table = 'api_permission'


class Application(SimplifyModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150, null=False)
    access_key = models.CharField(max_length=150, null=False)
    secret_access_key = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'application'


class AuthToken(SimplifyModel):
    id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=80, null=False)
    auth_type = models.CharField(max_length=150, null=True)
    user = models.ForeignKey('User', related_name='auth_token')
    updated = models.DateTimeField(null=True, blank=True)
    created = models.DateTimeField(null=False, default=timezone.now)

    def __repr__(self):
        return self.key

    class Meta:
        db_table = 'auth_token'


class Exercise(SimplifyModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', null=False, related_name='exercise')
    exercise_type = models.ForeignKey('ExerciseType', null=False, related_name='exercise')
    created = models.DateTimeField(default=timezone.now)
    start_time = models.DateTimeField(null=False, default=timezone.now)
    end_time = models.DateTimeField(null=True, blank=True)
    comments = models.CharField(max_length=255, null=True, blank=True)

    @property
    def score(self):
        if self.start_time and self.end_time and self.exercise_type:
            diff = self.end_time - self.start_time
            minutes = diff.total_seconds() / 60
            return round(minutes * float(self.exercise_type.multiplier), 2)
        else:
            return None

    @property
    def duration(self):
        if self.start_time and self.end_time:
            diff = self.end_time - self.start_time
            return round(diff.total_seconds() / 60, 2)
        else:
            return None

    @staticmethod
    def get_includes():
        return ['score', 'duration', 'exercise_type']

    @staticmethod
    def get_filters():
        return {
            'end_time__isnull': {
                'type': bool,
                'list': False
            },
            'start_time__gte': {
                'type': datetime.datetime,
                'list': False
            }
        }

    class Meta:
        db_table = 'exercise'


class ExerciseType(SimplifyModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    multiplier = models.DecimalField(decimal_places=2, max_digits=5)

    class Meta:
        db_table = 'exercise_type'


class FitnessPlan(SimplifyModel):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('User', null=False, related_name='fitness_plan')
    fitness_plan_type = models.ForeignKey('FitnessPlanType', null=False, related_name='fitness_plan')
    goal_weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(null=True, blank=True)

    @staticmethod
    def get_includes():
        return ['fitness_plan_type']

    class Meta:
        db_table = 'fitness_plan'


class FitnessPlanType(SimplifyModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    pounds_per_week = models.DecimalField(decimal_places=2, max_digits=5)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'fitness_plan_type'


class User(SimplifyModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    weight = models.DecimalField(decimal_places=2, max_digits=5, null=True, blank=True)
    active = models.BooleanField(null=False, default=True)
    created = models.DateTimeField(null=False, default=timezone.now)
    salt = models.CharField(max_length=50, null=True)
    password_reset_token = models.CharField(max_length=50, null=True)
    password_reset_token_created = models.DateTimeField(null=True)
    password_reset_ip = models.GenericIPAddressField(null=True)
    failed_login_attempts = models.IntegerField(null=True, default=0)
    last_failed_login = models.DateTimeField(null=True)

    # authentication requires an is_active field
    @property
    def is_active(self):
        return self.active

    class Meta:
        db_table = 'user'
