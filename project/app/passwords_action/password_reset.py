from django.contrib.auth import get_user_model
from db.serializers.password_reset_serializer import PasswordResetSerializer
from app.action import Action
from app.emails.verify_otp import VerifyOTP
from lib.lower_strip import strip_and_lower


class ResetPassword(Action):
    """The ResetPassword class accepts a request argument(data) and returns the user's data"""
    arguments = ['data']

    def perform(self):
        # Get the user instance in the database with the email address enter by the user, on the view
        user = get_user_model().objects.filter(email=strip_and_lower(self.data.get('email', '')))

        # Raise an error if there's no user with that email address in the database
        if not user.exists():
            self.fail(dict(invalid_email='Please enter a registered email address'))

        # Serialize the data - this carries out the validation
        serialize_password = PasswordResetSerializer(user[0], data=self.data)

        # Raise all errors from the serializer validation
        if not serialize_password.is_valid():
            self.fail(serialize_password.errors)

        # if there are no errors, verify the otp entered by the user
        verify_otp_user = VerifyOTP.call(otp_code=self.data.get('otp_code', ''))

        # If the otp verification failed, raise the error
        if verify_otp_user.failed:
            self.fail(dict(incorrect_otp='Your otp has either expired or is incorrect'))

        # If there are no errors, save the new password into the database
        serialize_password.save()

        return dict(data=None)
