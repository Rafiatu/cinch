from ..action import Action
from db.models.user import User
from db.models.account import Account
from db.models.artist import Artist
from db.serializers.user_serializer import UserSerializer
from db.serializers.account_serializer import AccountSerializer


class ArtistAccount(Action):
    arguments = ['user']

    def perform(self):
        user = self.user
        user_info = User.objects.get(id=user.id)
        artist_info = Artist.objects.get(user_id=user.id)
        
        try:
            account_info = Account.objects.get(artist_id=artist_info.id)
        except :
            self.fail(dict(account_error='Please add your account information'))

        serialize_user = UserSerializer(user_info)
        serialize_account = AccountSerializer(account_info)

        account_information = {
            'email': serialize_user.data.get('email', ''),
            'account_number': serialize_account.data.get('account_number', ''),
            'account_name': serialize_account.data.get('account_name', ''),
            'bank_name': serialize_account.data.get('bank_name', ''),
            'bank_code': serialize_account.data.get('bank_code', '')
        }

        return account_information
