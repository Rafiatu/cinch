from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from db.models.user import User
from rest_framework.authtoken.models import Token


class TestLogout(APITestCase):
    def setUp(self):
        user_data = {
            "username": "ResB",
            "email": "there@gmail.com",
            "phone_number": "+2348151107708",
            "password": "resa1234"
        }

        self.user = User.objects.create(**user_data)
        self.token = f'Token {Token.objects.create(user=self.user).key}'

    def test_logout(self):
        url = reverse('auth-logout')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout_twice(self):
        url = reverse('auth-logout')
        self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_without_token(self):
        url = reverse('auth-logout')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
