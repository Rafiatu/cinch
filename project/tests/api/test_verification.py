from datetime import timedelta
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from db.models.user import User
from db.serializers.user_serializer import UserSerializer

client = Client()


class TestVerifyEmail(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(
            email='deola@gmail.com', password='didi2828', otp_code='978299', username='didi',
            otp_code_expiry=timezone.now() + timedelta(minutes=10))

    def test_valid_otp_code(self):
        data = {
            'email': self.user1.email,
            'otp_code': self.user1.otp_code
        }
        response = client.post(
            reverse('otps-verify'), data)

        user = User.objects.get(pk=self.user1.pk)
        serializer = UserSerializer(user)
        self.assertEqual(response.data['message'], "success")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_email(self):
        data = {
            'email': "remi@gmail.com",
            'otp_code': self.user1.otp_code
        }
        response = client.post(reverse('otps-verify'), data)
        self.assertEqual(response.data['message'], 'failure')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_otp(self):
        data = {
            'email': "remi@gmail.com",
            'otp_code': "777777"
        }
        response = client.post(reverse('otps-verify'), data)
        self.assertEqual(response.data['message'], 'failure')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_otp_invalidemail(self):
        data = {
            'email': "",
            'otp_code': ""
        }
        response = client.post(reverse('otps-verify'), data)
        self.assertEqual(response.data['message'], 'failure')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
