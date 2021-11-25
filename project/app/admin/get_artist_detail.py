from ..action import Action
from django.db.models import Sum
from db.models.artist import Artist
from db.models.user import User
from db.models.location import Location
from db.models.songs import Song


class ArtistDetail(Action):
    arguments = ['artist_id']

    def perform(self):
        artist = Artist.objects.get(id=self.artist_id)
        user = User.objects.get(email=artist.user_id)
        song_count = artist.number_of_songs

        sum_streams = Song.objects.filter(
            artist_id=artist.id).aggregate(Sum('number_of_streams'))
        total_streams = sum_streams.get('number_of_streams__sum')

        try:
            location_id = artist.location_id_id
            location_info = Location.objects.get(pk=location_id)
            location = location_info.country
        except:
            location = 'None'

        artist_data = {
            'username': user.username,
            'email': user.email,
            'phone_number': str(user.phone_number),
            'number_of_songs_uploaded': song_count,
            'number_of_streams': total_streams,
            'location': location,
            'avatar':artist.avatar_url,
        }

        return artist_data
