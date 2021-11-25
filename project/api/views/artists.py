from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from app.artists.get_artist_profile import ArtistProfile
from app.admin.get_artist_detail import ArtistDetail
from app.admin.artists_monthly_song import ArtistSongPerMonth
from app.artists.get_artists import AllArtists
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.permissions.admin_permissions import IsUserAdmin
from rest_framework import status
from app.artists.update_artist import UpdateArtist
from api.lib.response import Response
from db.models.artist import Artist


class ArtistsViewSet(ViewSet):

    @action(methods=['get'], detail=False, url_path='detail')
    def get_artist(self, request):
        """
        This method gets all the details of a specific artist using their login token.
        """
        user = request.user
        result = ArtistProfile.call(user=user)

        if result.failed:
            return Response(
                errors=dict(errors=result.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data=result.value, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[IsUserAdmin], url_path='detail/(?P<artist_id>[0-9a-f\-]{32,})/')
    def get_artist_via_id(self, request, artist_id):
        """
            This method gets all the details of a specific artist using their ID.
        """
        result = ArtistDetail.call(artist_id=artist_id)

        if result.failed:
            return Response(errors=dict(errors=result.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=result.value, status=status.HTTP_200_OK)

    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated], url_path='update')
    def update_profile(self, request):
        request_email = request.user
        artist = UpdateArtist.call(data=request.data, user_email=request_email)

        if artist.failed:
            return Response(errors=dict(errors=artist.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=artist.value, status=status.HTTP_200_OK)
    
    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated], url_path='all-artists')
    def get_all_artists(self, request):
        """
            This method gets all the details of all artists
        """
        result = AllArtists.call()
        if result.failed:
            return Response(errors=dict(errors=result.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=result.value, status=status.HTTP_200_OK)

    @action(methods=['get'], detail=False, permission_classes=[IsUserAdmin, IsAuthenticated], url_path='analytics/(?P<artist_id>[0-9a-f\-]{32,})/')
    def get_artist_analytics_via_id(self, request, artist_id):
        """
            This method gets the data analytics of a specific artist using their ID.
        """
        info = ArtistSongPerMonth.call(artist_id=artist_id)

        if info.failed:
            return Response(errors=dict(errors=info.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=info.value, status=status.HTTP_200_OK)

