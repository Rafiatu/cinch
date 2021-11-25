from app.action import Action
from db.models.account import Account
from db.serializers.account_serializer import AccountSerializer


class GetAccount(Action):
    def perform(self):
        all_accounts = Account.objects.all()
        serialize_accounts = AccountSerializer(all_accounts, many=True)
        return dict(accounts=serialize_accounts.data)
