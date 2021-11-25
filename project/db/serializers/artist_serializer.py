from rest_framework import serializers
from ..models.artist import Artist


class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'

class ArtistDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
        depth=1

