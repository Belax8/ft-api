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


class User(SimplifyModel):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=80, null=True)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
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
