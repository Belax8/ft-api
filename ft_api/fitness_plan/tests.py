import configurations
import django
import os
import random

os.environ['DJANGO_SETTINGS_MODULE'] = 'ft_api.settings'
# setup the configuration local
os.environ['DJANGO_CONFIGURATION'] = 'Local'
configurations.setup()
django.setup()

from rest_framework_signature.helpers import RestFrameworkSignatureTestClass
from rest_framework import status

from ft_api.test.helpers import DataGenerator


class FitnessPlanTests(RestFrameworkSignatureTestClass):

    def test_get(self):
        # arrange
        fitness_plan = DataGenerator.set_up_fitness_plan()
        url = '/fitnessPlans/{0}'.format(fitness_plan.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['id'], fitness_plan.id)

    def test_get_list_sub(self):
        # arrange
        user = DataGenerator.set_up_user()
        fitness_plan = DataGenerator.set_up_fitness_plan(user=user)
        url = '/users/{0}/fitnessPlans'.format(user.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data[0]['id'], fitness_plan.id)

    def test_put(self):
        # arrange
        fitness_plan = DataGenerator.set_up_fitness_plan()
        url = '/fitnessPlans/{0}'.format(fitness_plan.id)
        body = {
            'goalWeight': random.randint(1, 1000)
        }
        headers = self.get_headers(url, body)

        # act
        result = self.api_client.put(url, body, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['goalWeight'], body['goalWeight'])

    def test_post(self):
        # arrange
        user = DataGenerator.set_up_user()
        fitness_plan_type = DataGenerator.set_up_fitness_plan_type()
        url = '/fitnessPlans'
        body = {
            'userId': user.id,
            'fitnessPlanTypeId': fitness_plan_type.id,
            'goalWeight': random.randint(1, 1000)
        }
        headers = self.get_headers(url, body)

        # act
        result = self.api_client.post(url, body, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
