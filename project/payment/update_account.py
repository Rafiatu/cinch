from db.serializers.account_serializer import AccountSerializer
from app.action import Action
from db.models.artist import Artist
from db.models.account import Account


class UpdateAccount(Action):
    arguments = ['user_email', 'bank_data']

    def perform(self):
        artist = Artist.objects.get(user_id=self.user_email)
        account = Account.objects.get(artist_id=artist.id)

        account_serializer = AccountSerializer(account, data=self.bank_data, partial=True)

        if account_serializer.is_valid():
            account_serializer.save()
        else:
            self.fail(account_serializer.errors)

        success_data = dict(
            account_name=self.bank_data.get('account_name'),
            account_number=self.bank_data.get('account_number'),
            bank_name=self.bank_data.get('bank_name')
        )

        return success_data
