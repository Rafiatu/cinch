from django.contrib.auth import get_user_model
from django.utils import timezone

from app.action import Action


class VerifyOTP(Action):
    arguments = ['otp_code']

    def perform(self):
        user = get_user_model().objects.filter(otp_code=self.otp_code)

        if not user.exists():
            self.fail(dict(invalid_otp='Please provide a valid OTP'))

        expiry_time = user[0].otp_code_expiry
        if expiry_time > timezone.now():
            return dict(otp=self.otp_code)
        else:
            self.fail(dict(expired_otp='OTP provided has been expired'))
