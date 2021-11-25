from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from db.models.user import User

class TestGetBankList(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='user@xyz.com',
            username='user1',
            password='reallife1'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()


    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_get_bank_list(self):
        url = reverse('banks-get-bank-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)