from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from db.models.user import User


class TestAllArtists(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@xyz.com',
            username='user1',
            password='endsars1'
        )
        self.token = f'Token {Token.objects.create(user=self.user).key}'

    def test_get_all_artists(self):
        url= reverse('artists-get-all-artists')
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
