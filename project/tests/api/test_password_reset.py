from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from db.models.user import User


class TestPasswordReset(APITestCase):
    def setUp(self) -> None:
        data = {'email': 'tester@test.com', 'username': 'test', 'phone_number': '+2347066543217', 'password': 'qazxsw111','otp_code':'123456', 'otp_code_expiry': timezone.now()+timedelta(minutes=10)}
        self.user = User.objects.create(**data)
        self.user.save()

    def test_correct_data(self):
        url = reverse('passwords-reset')
        otp_code = get_user_model().objects.get().otp_code
        email = get_user_model().objects.get().email

        data = {'otp_code': otp_code, 'email': email, 'password': 'jumper48', 'confirm_password': 'jumper48'}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_otp(self):
        url = reverse('passwords-reset')
        email = get_user_model().objects.get().email
        data = {'otp_code': '123', 'email': email, 'password': 'jumper48', 'confirm_password': 'jumper48'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_email(self):
        url = reverse('passwords-reset')
        otp_code = get_user_model().objects.get().otp_code
        data = {'otp_code': otp_code, 'email': 'trump@yahoo.com', 'password': 'jumper48', 'confirm_password': 'jumper48'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_password(self):
        url = reverse('passwords-reset')
        otp_code = get_user_model().objects.get().otp_code
        email = get_user_model().objects.get().email
        data = {'otp_code': otp_code, 'email': email, 'password': 'w1', 'confirm_password': 'jumper48'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_confirm_password(self):
        url = reverse('passwords-reset')
        otp_code = get_user_model().objects.get().otp_code
        email = get_user_model().objects.get().email
        data = {'otp_code': otp_code, 'email': email, 'password': 'jumper48', 'confirm_password': 'jumper8'}
        response = self.client.put(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
