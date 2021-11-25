from .payment_interface import PaymentInterface
from app.action import Action


class BankList(Action):
    def perform(self):
        try:
            res = PaymentInterface.get('https://api.paystack.co/bank')
            banks = res.get('data')
            bank_data = [{'id': bank.get('id'), 'name' : bank.get('name'), 'code': bank.get('code'), 'active': bank.get('active'), 'pay_with_bank': bank.get('pay_with_bank'), 'country': bank.get('country')} for bank in banks]
            return bank_data
        except:
            return self.fail(dict(paystack_error='Having problems connecting to paystack'))
