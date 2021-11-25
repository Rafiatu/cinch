from rest_framework.viewsets import ViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from api.permissions.admin_permissions import IsUserAdmin
from app.admin.total_songs import TotalSongs
from app.artists.total_artistes import TotalArtistes
from app.admin.songs_per_month import MonthlySongs
from app.admin.users_per_month import MonthlyUsers


class DataAnalyticsViewSet(ViewSet):
    @action(methods=['get'], detail=False, permission_classes=[IsUserAdmin])
    def app_data(self, request):
        total_artisans = TotalArtistes.perform(self, request)
        total_songs = TotalSongs.perform(self, request)
        monthly_songs = MonthlySongs.perform(self, request)
        users = MonthlyUsers.perform(self, request)

        info = {"Total Number of Artistes": total_artisans,
                "Total Number of Songs": total_songs,
                "Songs per month": monthly_songs,
                "Users per month": users
                }
        return Response(
            data=info,
            status=status.HTTP_200_OK
        )
