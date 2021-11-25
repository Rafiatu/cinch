from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from db.models.user import User
from db.models.artist import Artist


class TestCreateAccount(APITestCase):
    def setUp(self):
        user_data = {
            "email": "there@gmail.com",
            "password": "resa1234",
            "otp_code":"978299"
        }

        self.user = User.objects.create(**user_data)

        artist_data = {
            "user_id": self.user,
            "firstname": "Resa",
            "lastname": "Obas",
            "avatar_url": "http://test.com"
        }

        self.artist = Artist.objects.create(**artist_data)

        self.wrong_data = {
            "account_number": "02216652",
            "bank_code": "058",
            "bank_name": "GTB Bank"
        }
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_add_invalid_account(self):
        url = reverse('accounts-create-account')
        response = self.client.post(url, self.wrong_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


