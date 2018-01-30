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


class UserTests(RestFrameworkSignatureTestClass):

    def test_get(self):
        # arrange
        user = DataGenerator.set_up_user()
        url = '/users/{0}'.format(user.id)
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['id'], user.id)

    def test_get_list(self):
        # arrange
        DataGenerator.set_up_user()
        url = '/users'
        headers = self.get_headers(url)

        # act
        result = self.api_client.get(url, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertTrue(len(result.data) > 0)

    def test_put(self):
        # arrange
        user = DataGenerator.set_up_user()
        url = '/users/{0}'.format(user.id)
        body = {
            'weight': random.randint(1, 1000)
        }
        headers = self.get_headers(url, body)

        # act
        result = self.api_client.put(url, body, format='json', **headers)

        # assert
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        self.assertEqual(result.data['weight'], body['weight'])
