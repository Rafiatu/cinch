from db.serializers.artist_serializer import ArtistSerializer
from db.serializers.user_serializer import UpdateUserSerializer
from app.action import Action
from db.models.artist import Artist
from db.models.user import User


class UpdateArtist(Action):
    arguments = ['data', 'user_email']

    def perform(self):
        if not self.data.get('avatar_url', ''):
            self.fail(dict(invalid_image='Please provide an Image'))

        artist = Artist.objects.get(user_id=self.user_email)
        user = User.objects.get(email=self.user_email)

        artist_serializer = ArtistSerializer(artist, data=self.data, partial=True)
        user_serializer = UpdateUserSerializer(user, data=self.data, partial=True)

        if user_serializer.is_valid():
            user_serializer.save()
        else:
            self.fail(user_serializer.errors)

        if artist_serializer.is_valid():
            artist_serializer.save()
        else:
            self.fail(artist_serializer.errors)

        first_name = artist_serializer.data.get('firstname')
        last_name = artist_serializer.data.get('lastname')

        success_data = dict(
            first_name=first_name,
            last_name=last_name,
            location_id=self.data.get('location_id'),
            avatar_url=self.data.get('avatar_url'),
            phone_number=self.data.get('phone_number')
        )

        return success_data
