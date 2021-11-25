from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import status
from app.passwords_action.password_reset import ResetPassword
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action, permission_classes
from api.lib.response import Response
from app.password_action import password_update_action


class PasswordsViewSet(ViewSet):
    @action(methods=['put'], detail=False, permission_classes=[IsAuthenticated])
    def change(self, request):
        """ 
        This method updates the user's password and returns an appropriate response.
        """
        user = request.user
        data = request.data
        result = password_update_action.UpdatePassword.call(user=user, data=data)

        if result.failed:
            return Response(
                errors=dict(errors=result.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data=result.value, status=status.HTTP_201_CREATED)

    @action(methods=['put'], detail=False, permission_classes=[AllowAny])
    def reset(self, request):
        """This reset password view collects the data from the user and calls the ResetPassword Action
        to perform the necessary validations on the data."""
        data = request.data

        result = ResetPassword.call(data=data)

        # If the action fails, it should return the error with its status
        if result.failed:
            return Response(
                errors=dict(errors=result.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )

        # else it should return the data with its status
        return Response(
            data=result.value,
            status=status.HTTP_201_CREATED
        )
