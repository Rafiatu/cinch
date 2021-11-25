from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestGetAccounts(APITestCase):
    def test_get_accounts(self):
        url = reverse('accounts-get-accounts')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)