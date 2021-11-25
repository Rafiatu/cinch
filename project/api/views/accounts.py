from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from api.lib.response import Response
from payment.get_accounts import GetAccount
from payment.create_account import CreateAccount
from payment.update_account import UpdateAccount
from payment.account_verification import AccountVerification
from app.artists.get_artist_account import ArtistAccount


class AccountViewSet(ViewSet):

    @action(methods=['get'], detail=False, permission_classes=[AllowAny], url_path='*')
    def get_accounts(self, request):
        result = GetAccount.call()
        return Response(result.value, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='create')
    def create_account(self, request):

        account_details = AccountVerification.call(data=request.data)
        if account_details.failed:
            return Response(errors=dict(errors=account_details.error.value), status=status.HTTP_400_BAD_REQUEST)

        res = account_details.value
        user_data = res.get('data')
        account_number, account_name = user_data.get('account_number'), user_data.get('account_name')
        bank_name, bank_code = request.data.get('bank_name'), request.data.get('bank_code')
        user_id = request.user.id
        save_data = CreateAccount.call(account_name=account_name, account_number=account_number,
                                       bank_name=bank_name, bank_code=bank_code, user_id=user_id)

        if save_data.failed:
            return Response(errors=dict(errors=save_data.error.value), status=status.HTTP_400_BAD_REQUEST)
        return Response(data=save_data.value, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False, url_path='detail')
    def get_artist_account(self, request):
        user = request.user

        result = ArtistAccount.call(user=user)

        if result.failed:
            return Response(
                errors=dict(errors=result.error.value),
                status=status.HTTP_400_BAD_REQUEST
            )
        return Response(data=result.value, status=status.HTTP_200_OK)
        
    @action(methods=['put'], detail=False, url_path='update')
    def update_account(self, request):
        request_email = request.user
        account_details = AccountVerification.call(data=request.data)

        if account_details.failed:
            return Response(errors=dict(errors=account_details.error.value), status=status.HTTP_400_BAD_REQUEST)

        res = account_details.value
        account_data = res.get('data')

        bank_data = dict(
            account_number=account_data.get('account_number'),
            account_name=account_data.get('account_name'),
            bank_name=request.data.get('bank_name'),
            bank_code=request.data.get('bank_code')
        )

        account = UpdateAccount.call(user_email=request_email, bank_data=bank_data)

        if account.failed:
            return Response(errors=dict(errors=account.error.value), status=status.HTTP_400_BAD_REQUEST)

        return Response(data=account.value, status=status.HTTP_200_OK)
