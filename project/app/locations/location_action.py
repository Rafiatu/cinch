from app.action import Action
from db.models.location import Location
from db.serializers.location_serializer import LocationSerializer


class GetLocation(Action):

    def perform(self):
        all_locations = Location.objects.all()
        serialize_location = LocationSerializer(all_locations, many=True)
        return dict(location=serialize_location.data)
