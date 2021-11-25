from app.action import Action
from db.models.artist import Artist
from db.serializers.song_serializer import SongSerializer
from db.serializers.artist_serializer import ArtistSerializer


class UploadSong(Action):
    arguments = ['data', 'user_email']

    def perform(self):
        artist_instance = Artist.objects.get(user_id=self.user_email)
        artist = Artist.objects.get(user_id=self.user_email).id

        title = self.data.get('title', '')

        new_data = dict(
            url=self.data.get('song_url'),
            cover_art_url=self.data.get('image_url'),
            title=title,
            artist_id=artist
        )

        song_serializer = SongSerializer(data=new_data)

        if not song_serializer.is_valid():
            self.fail(song_serializer.errors)

        song_serializer.save()

        # update song count as song upload occurs
        update_song_count = artist_instance.number_of_songs + 1
        artist_data = {
            'number_of_songs': update_song_count
        }
        # save new song count to artist table
        artist_serializer = ArtistSerializer(artist_instance, data=artist_data, partial=True)

        if not artist_serializer.is_valid():
            self.fail(artist_serializer)

        artist_serializer.save()

        return new_data
