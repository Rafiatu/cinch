from datetime import timedelta
from django.test import Client
from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from db.models.user import User
from db.serializers.user_serializer import UserSerializer


client = Client()

class TestSendOtp(APITestCase):
    
    def setUp(self):
        self.ade = User.objects.create(
            email='deohr@gmail.com', password='dero12345', otp_code='978299', username='drro',
            otp_code_expiry=timezone.now() + timedelta(minutes=10))
        
        self.adeope = User.objects.create(
            email='', password='dero12345', otp_code='978699', username='adeoo',
            otp_code_expiry=timezone.now() + timedelta(minutes=10))

    def test_valid_otp_code(self):
        data = {
            'email': self.ade.email
        }
        response = client.post(reverse('otps-send'), data)
        user = User.objects.get(pk=self.ade.pk)
        serializer = UserSerializer(user)
        
        self.assertEqual(response.data.get('data').get("otp"), serializer.data.get('otp_code'))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_invalid_otp_code(self):
        data = {
            'email': self.adeope.email
        }
        response = client.post(reverse('otps-send'), data)
        self.assertEqual(response.data['message'], 'failure')
        