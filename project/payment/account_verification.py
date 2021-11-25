from .payment_interface import PaymentInterface
from app.action import Action


class AccountVerification(Action):
    arguments = ['data']

    def perform(self):
        account_number = self.data.get('account_number')
        bank_code = self.data.get('bank_code')

        res_url = f'https://api.paystack.co/bank/resolve?account_number={account_number}&bank_code={bank_code}'

        result = PaymentInterface.get_with_auth(res_url)

        status_message = result.get('status')

        # If Pay stack account verification fails
        if not status_message:
            self.fail(dict(invalid_account='Sorry, It seems you have entered an incorrect Bank Detail.'))

        # else return the data from paystack
        return result
