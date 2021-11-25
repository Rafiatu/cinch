from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework import status

from api.lib.response import Response
from api.permissions.admin_permissions import IsUserAdmin

from app.admin.register_admin_action import RegisterAdmin
from app.auth.register import Register
from app.auth.login import Login
from app.auth.logout import LogoutAction


class AuthsViewSet(ViewSet):
    permission_classes = [AllowAny]

    @action(methods=['post'], detail=False)
    def login(self, request):
        '''Generates a token based on the email and password passed in as parameters.
        e.g: {'email': 'enter_email_here', 'password': 'your_password'}'''
        login_details = Login.call(data=request.data)
        if login_details.failed:
            return Response(
                errors=dict(errors=login_details.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(
            data=login_details.value,
            status=status.HTTP_200_OK
        )

    @action(methods=['post'], detail=False)
    def register(self, request):
        artist = Register.call(data=request.data)
        
        if artist.failed:
            return Response(
                errors=dict(errors=artist.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )

        return Response(
            data=artist.value, 
            status=status.HTTP_201_CREATED
        )

    @action(methods=['post'], detail=False, permission_classes=[IsUserAdmin], url_path='register/admin')
    def register_admin(self, request):
        admin = RegisterAdmin.call(data=request.data)

        if admin.failed:
            return Response(
                errors=dict(error=admin.error.value),
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            data=admin.value,
            status=status.HTTP_201_CREATED
        )

    @action(methods=['get'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout_user = LogoutAction.call(request=request)

        if logout_user.failed:
            return Response(
                errors=dict(error=logout_user.error.value),
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            data=logout_user.value,
            status=status.HTTP_200_OK
        )
