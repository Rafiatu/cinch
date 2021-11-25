from payment.payment_interface import PaymentInterface
from rest_framework.test import APITestCase


class TestPaymentInterface(APITestCase):

    def test_get(self):
        res = PaymentInterface.get('https://api.paystack.co/bank')
        self.assertEquals(res.get('status'), True)

    def test_get_with_auth(self):
        res = PaymentInterface.get_with_auth(
            'https://api.paystack.co/bank/resolve?account_number=310484182&bank_code=011')
        self.assertEquals(res.get('status'), False)
