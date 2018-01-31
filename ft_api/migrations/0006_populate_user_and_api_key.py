import uuid

from django.db import migrations, models


def create_user_and_api_key(apps, schema_editor):
    # You wouldn't do this in a real app
    User = apps.get_model('ft_api', 'User')
    ApiKey = apps.get_model('ft_api', 'ApiKey')
    AuthToken = apps.get_model('ft_api', 'AuthToken')

    # Setup user
    username = 'chris@testing.com'
    salt = 'm7xEb8gjTCn2+ZUBPtvRQg1Z6hHnBlNdSoQPDnEe2Qw='
    password = 'c3fcca9dc3b61527cfed6f1128d2a1b21f8723c5'  # test123

    try:
        user = User.objects.get(username=username)
        user.password = password
        user.salt = salt
    except:
        user = User(username=username, password=password, salt=salt, first_name='Chris', last_name='Johnson')

    user.save()

    # Setup API Key
    api_key = ApiKey(name='ft-app', access_key='b44493b5-4', secret_access_key='fd4f4b5d-4ef4-4866-8')
    api_key.save()

    # Setup Auth Token
    auth_token = AuthToken(key=str(uuid.uuid4())[:20], auth_type='password', user=user)
    auth_token.save()


class Migration(migrations.Migration):
    dependencies = [
        ('ft_api', '0005_populate_fitness_plans')
    ]

    operations = [
        migrations.RunPython(create_user_and_api_key, reverse_code=migrations.RunPython.noop),
    ]


