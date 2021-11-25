from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class TestLogin(APITestCase):
    """Tests the login endpoint to see that it generates token when it's supposed to."""
    def test_login_user(self):
        """Currently, there are no user records in the database so it should return bad request"""
        url = reverse('auth-login')
        data = {
            "email": "bella@here.com",
            "password": "password"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_empty_params(self):
        url = reverse('auth-login')
        data = {
            "email": "",
            "password": ""
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_no_input(self):
        url = reverse('auth-login')
        data = {}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_wrong_password(self):
        url = reverse('auth-login')
        data = {
            "email": "decagon.uno@hq.com",
            "password": "internship"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login_wrong_email(self):
        url = reverse('auth-login')
        data = {
            "email": "decagoon@yahoo.com",
            "password": "bootcamp"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)