import configurations
import django
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ft_api.settings'
# setup the configuration local
os.environ['DJANGO_CONFIGURATION'] = 'Local'
configurations.setup()
django.setup()

from rest_framework_signature.helpers import RestFrameworkSignatureTestClass
from rest_framework import status

from ft_api.domain.models import Exercise
from ft_api.test.helpers import DataGenerator


class ExerciseTests(RestFrameworkSignatureTestClass):

    def test_get(self):
        # arrange
        exercise = DataGenerator.set_up_exercise()
        url = '/exercises/{0}'.format(exercise.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['id'], exercise.id)

    def test_get_include_score(self):
        # arrange
        exercise = DataGenerator.set_up_exercise()
        url = '/exercises/{0}?include=score'.format(exercise.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['id'], exercise.id)
        db_exercise = Exercise.objects.get(id=exercise.id)
        self.assertEqual(result.data['score'], db_exercise.score)

    def test_get_list_sub(self):
        # arrange
        user = DataGenerator.set_up_user()
        DataGenerator.set_up_exercise(user=user)
        url = '/users/{0}/exercises'.format(user.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertTrue(len(result.data) > 0)
