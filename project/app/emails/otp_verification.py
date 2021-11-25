from django.contrib.auth import get_user_model

from app.action import Action
from app.emails.verify_otp import VerifyOTP


class VerifyEmailVerify(Action):
    arguments = ['email', 'otp']

    def perform(self):
        user = get_user_model().objects.filter(email=self.email)

        if not user.exists():
            self.fail(dict(invalid_email='Please provide a valid and / or registered email'))

        user = user[0]

        if user.otp_code != self.otp:
            self.fail(dict(invalid_otp='Please provide a valid OTP'))

        otp_expired = VerifyOTP.call(otp_code=self.otp)

        if otp_expired.failed:
            self.fail(dict(otp_expired='OTP provided has been expired'))

        user.email_verified = True
        user.save()
        return dict(data=None)
