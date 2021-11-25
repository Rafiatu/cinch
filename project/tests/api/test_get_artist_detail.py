from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from db.models.user import User
from db.models.artist import Artist
from db.models.location import Location
from rest_framework.authtoken.models import Token


class TestGetArtistDetail(APITestCase):
    def setUp(self):

        user_data = {
            "username": "ResB",
            "email": "there@gmail.com",
            "phone_number": "+2348151107708",
            "password": "resa1234"
        }

        self.user = User.objects.create(**user_data)

        admin = {
            "email": "resab@gmail.com",
            "password": "resab1234",
            "is_superadmin": True,
            "email_verified": True
        }

        self.admin = User.objects.create(**admin)

        self.location = Location.objects.create(
            id='234',
            country='Nigeria',
            country_code='+234'
        )

        artist_data = {
            "user_id":self.user,
            "firstname": "Resa",
            "lastname": "Obas",
            "avatar_url": "http://test.com",
            "location_id": self.location
        }

        self.artist = Artist.objects.create(**artist_data)

        self.token = f'Token {Token.objects.create(user=self.admin).key}'
        self.fake_token = f'Token {Token.objects.create(user=self.user).key}'

    def test_get_artist_details(self):
        url = reverse('artists-get-artist-via-id', kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_artist_correct_details(self):
        url = reverse('artists-get-artist-via-id', kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get('data')['username'], 'ResB')

    def test_without_authorization(self):
        url = reverse('artists-get-artist-via-id', kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.fake_token, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
