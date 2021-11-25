from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from db.models.user import User
from db.models.artist import Artist
from db.models.location import Location
from rest_framework.authtoken.models import Token


class TestArtistAnalyticsEndpoint(APITestCase):
    def setUp(self):
        user_data = {
            "username": "Data Science",
            "email": "artistanalysis@gmail.com",
            "phone_number": "+2348151107708",
            "password": "analytics1234"
        }

        self.user = User.objects.create(**user_data)
        self.user_token = f'Token {Token.objects.create(user=self.user).key}'

        admin = {
            "email": "artistanalytics@gmail.com",
            "password": "decagon1234",
            "is_superadmin": True,
            "email_verified": True
        }
        self.location = Location.objects.create(
            id='234',
            country='Nigeria',
            country_code='+234'
        )

        artist_data = {
            "user_id": self.user,
            "firstname": "Data",
            "lastname": "Science",
            "avatar_url": "http://www.testimage.com",
            "location_id": self.location
        }

        self.artist = Artist.objects.create(**artist_data)

        self.admin = User.objects.create(**admin)
        self.admin_token = f'Token {Token.objects.create(user=self.admin).key}'

    def test_user_is_authenticated_not_admin(self):
        url = reverse('artists-get-artist-analytics-via-id',  kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.user_token)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_is_authenticated_and_admin(self):
        url = reverse('artists-get-artist-analytics-via-id',  kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION=self.admin_token, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_not_authenticated(self):
        url = reverse('artists-get-artist-analytics-via-id',  kwargs={"artist_id": self.artist.id})
        response = self.client.get(url, HTTP_AUTHORIZATION='', format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
