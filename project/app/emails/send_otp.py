from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

from app.action import Action
from lib.generate_otp import generate_otp
from app.emails.email_template import email_template


class SendOTP(Action):
    arguments = ['email', 'otp']

    def perform(self):

        if not self.email:
            self.fail(dict(invalid_email='Please provide a valid email address'))

        user = get_user_model().objects.filter(email=self.email)
        if not user.exists():
            self.fail(dict(invalid_email='Please provide a valid email'))
        
        user = user[0]
        otp = self.otp
        if otp is None:
            otp = generate_otp()

        user.otp_code = otp
        expiry = timezone.now() + timedelta(minutes=10)
        user.otp_code_expiry = expiry
        user.email_verified = False
        user.save()

        otp_value = user.otp_code
        email = self.email
        email_subject = 'Cinch Email Verification'
        username = user.username

        email_body = f'''
            Hi {username}, Welcome to Cinch, we are delighted to have you on board.
            <br><br>Here is your OTP Code:<strong>{otp_value}</strong> 
            <br><br><b>Note: <i>This OTP expires in 10 minutes</i> </b>'''

        email_template(email_subject, email, email_body)

        return otp_value
