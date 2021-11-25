from app.action import Action
from db.models.artist import Artist
from db.models.account import Account
from db.serializers.account_serializer import AccountSerializer


class CreateAccount(Action):
    arguments = ['account_name', 'account_number', 'bank_name', 'bank_code', 'user_id']

    def perform(self):
        artist_id = Artist.objects.get(user_id=self.user_id)

        # Get all the Data
        account_name = self.account_name
        account_number = self.account_number
        bank_name = self.bank_name
        bank_code = self.bank_code
        artist_id = artist_id

        data = dict(
            account_name=self.account_name,
            account_number=self.account_number,
            bank_name=self.bank_name,
            bank_code=self.bank_code,
            artist_id=artist_id.id
        )

        account_serializer = AccountSerializer(data=data)

        if not account_serializer.is_valid():
            self.fail(account_serializer.errors)

        account = Account.objects.create(
            account_name=account_name,
            account_number=account_number,
            bank_name=bank_name,
            bank_code=bank_code,
            artist_id=artist_id
        )

        # save user to db
        account.save()

        return_message = dict(
            message='Your Bank Account Details have been saved successfully'
        )
        return return_message
