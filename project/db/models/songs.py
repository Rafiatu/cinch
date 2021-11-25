import uuid
from django.db import models
from db.models.artist import Artist


class Song(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True)
    url = models.URLField()
    cover_art_url = models.URLField()
    number_of_streams = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title
