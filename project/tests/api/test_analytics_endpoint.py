from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from db.models.user import User
from rest_framework.authtoken.models import Token


class TestAnalyticsEndpoint(APITestCase):
    def setUp(self):
        user_data = {
            "username": "Data Science",
            "email": "analysis@gmail.com",
            "phone_number": "+2348151107708",
            "password": "analytics1234"
        }

        self.user = User.objects.create(**user_data)
        self.user_token = f'Token {Token.objects.create(user=self.user).key}'

        admin = {
            "email": "analytics@gmail.com",
            "password": "decagon1234",
            "is_superadmin": True,
            "email_verified": True
        }

        self.admin = User.objects.create(**admin)
        self.token = f'Token {Token.objects.create(user=self.admin).key}'

    def test_accessed_by_admin(self):
        url = reverse('analytics-app-data')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_accessed_by_normal_user(self):
        url = reverse('analytics-app-data')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.user_token, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauthenticated_user(self):
        url = reverse('analytics-app-data')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
