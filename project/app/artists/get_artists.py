from ..action import Action
from db.models.artist import Artist
from db.models.user import User
from db.serializers.artist_serializer import ArtistDetailsSerializer


class AllArtists(Action):
    def perform(self):
        all_artists = Artist.objects.all()
        serialize_artists = ArtistDetailsSerializer(all_artists, many=True)
        return dict(artists=serialize_artists.data)
