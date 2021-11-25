from ..action import Action
from db.serializers.password_serializer import PasswordSerializer


class UpdatePassword(Action):
    """
    This class contains the logic that would be used by the view.
    """
    arguments = ['user', 'data']

    def perform(self):
        """
        This method validates the serializer data and raises appropriate errors
        """

        serializer = PasswordSerializer(self.user, data=self.data, many=False, context={
            'user': self.user
        }, partial=True)

        if serializer.is_valid():
            serializer.save()
            return {'data': None}
        else:
            self.fail(serializer.errors)





