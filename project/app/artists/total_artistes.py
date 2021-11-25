from ..action import Action
from db.models.artist import Artist


class TotalArtistes(Action):
    arguments = []
    def perform(self, request):
        artistes = len(Artist.objects.all())
        return artistes
