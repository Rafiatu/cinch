import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status

from db.models.user import User
from db.serializers.password_serializer import PasswordSerializer


class PasswordUpdateApiTest(APITestCase):
    """
    This class contains methods to test the update password API
    """

    def setUp(self):
        self.user = User.objects.create_user(
            email='user@xyz.com',
            username='user1',
            password='endsars1'
        )
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_pass(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
                                                                "confirm_password": "endsars2"})
        response.render()
        self.assertIsNone(response.data['errors'])
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['message'], 'success')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_fail_old_password(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars3", "password": "endsars2",
                                                                "confirm_password": "endsars2"})
        response.render()
        self.assertIsNotNone(response.data['errors'])
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['message'], 'failure')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_new_passwords_no_match(self):
        response = self.client.put('/api/v1/passwords/change', {"old_password": "endsars1", "password": "endsars2",
                                                                "confirm_password": "endsars3"})
        response.render()
        self.assertIsNotNone(response.data['errors'])
        self.assertIsInstance(response.data, dict)
        self.assertEqual(response.data['message'], 'failure')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

