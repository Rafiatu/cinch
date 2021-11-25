from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestCreateLocation(APITestCase):
    def setUp(self):
        url = reverse('locations-create-location')
        data = {'id': '266', 'country': 'Lesotho', 'country_code': '+266'}
        self.client.post(url, data, format='json')

    def test_create_location(self):
        url = reverse('locations-create-location')
        data = {'id': '234', 'country': 'Nigeria', 'country_code': '+234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_same_code(self):
        url = reverse('locations-create-location')
        data = {'id': '260', 'country': 'South Africa', 'country_code': '+266'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incomplete_request(self):
        url = reverse('locations-create-location')
        data = {'country': 'Lesotho', 'country_code': '+266'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
