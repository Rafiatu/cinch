from app.action import Action
from db.serializers.location_serializer import LocationSerializer


class CreateLocation(Action):
    arguments = ['data']

    def perform(self):
        self.data['country'] = self.data['country'].title()

        serialize_location = LocationSerializer(data=self.data)

        if serialize_location.is_valid():
            serialize_location.save()

        else:
            self.fail(serialize_location.errors)

        return_data = dict(
            message='Location has been successfully saved.'
        )

        return return_data
