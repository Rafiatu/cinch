from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from db.models.user import User
from db.models.artist import Artist
from db.models.location import Location


class TestGetAccounts(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='user@xyz.com',
            username='user1',
            password='endsars1'
        )
        self.location = Location.objects.create(
            id = '234',
            country='Nigeria',
            country_code='+234'
        )
        Artist.objects.create(
            user_id=self.user,
            location_id=self.location,
        )

    def test_get_accounts(self):
        url = reverse('artists-get-artist')
        self.client.force_authenticate(self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)