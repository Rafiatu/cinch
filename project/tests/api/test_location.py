from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestLocation(APITestCase):
    def test_get_location(self):
        url = reverse('locations-get-location')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
