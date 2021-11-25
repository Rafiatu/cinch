from ..action import Action
from db.models.songs import Song


class TotalSongs(Action):
    def perform(self, request):
        songs = len(Song.objects.all())
        return songs
