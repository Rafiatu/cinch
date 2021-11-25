from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse
from db.models.user import User

class TestCreateAdmin(APITestCase):
    def setUp(self):

        admin = {
            "email": "resb@gmail.com",
            "password": "resabb1234",
            "is_superadmin": True,
            "email_verified": True
        }
        self.admin = User.objects.create(**admin)

        self.data = dict(
            email='user@xyz.com',
            first_name='user1',
            last_name='reallife1'
        )

        self.token = f'Token {Token.objects.create(user=self.admin).key}'

        def test_register_admin(self):
            url = reverse('auth-register-admin')
            response = self.client.post(url, self.data, HTTP_AUTHORIZATION=self.token, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_creates_admin(self):
            url = reverse('auth-register-admin')
            response = self.client.post(url, self.data, HTTP_AUTHORIZATION=self.token, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data.get('data')['username'], 'user1reallife1')
