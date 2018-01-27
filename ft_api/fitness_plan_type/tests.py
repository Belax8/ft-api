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

from ft_api.test.helpers import DataGenerator


class FitnessPlanTypeTests(RestFrameworkSignatureTestClass):

    def test_get(self):
        # arrange
        fitness_plan_type = DataGenerator.set_up_fitness_plan_type()
        url = '/fitnessPlanTypes/{0}'.format(fitness_plan_type.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['id'], fitness_plan_type.id)

    def test_get_list(self):
        # arrange
        DataGenerator.set_up_fitness_plan_type()
        url = '/fitnessPlanTypes'
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertTrue(len(result.data) > 0)
