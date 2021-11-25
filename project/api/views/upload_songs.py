from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from app.uploads import upload_song_action
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from api.lib.response import Response


class UploadSongsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, JSONParser,)

    @action(methods=['post'], detail=False, url_path='*')
    def upload(self, request, format=None):

        user_email = request.user
        uploads = upload_song_action.UploadSong.call(data=request.data, user_email=user_email)
        if uploads.failed:
            return Response(errors=dict(errors=uploads.error.value),
                status = status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=uploads.value,
            status=status.HTTP_200_OK)
