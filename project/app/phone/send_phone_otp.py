from datetime import timedelta
from django.conf import settings
from django.utils import timezone

from twilio.rest import Client

from app.action import Action
from db.models.user import User
from app.emails.send_otp import SendOTP
from lib.generate_otp import generate_otp
from db.models.location import Location
from db.serializers.phone_number_serializer import PhoneNumberSerializer


class PhoneOtpAction(Action):
    arguments = ['data', 'otp']

    def perform(self):
        email_exist = 'email' in self.data and self.data['email']
        location_exist = 'location_id' in self.data and self.data['location_id']

        if not email_exist:
            self.fail(dict(invalid_email='Please provide an email'))

        user = self.get_queryset(self.data['email']) #gets instance of user
        if not user:
            self.fail(dict(invalid_email='Please provide a valid email'))

        if not location_exist:
            self.fail(dict(invalid_location='Please enter a location'))

        phone_number_valid = PhoneNumberSerializer(data=self.data)
        if not phone_number_valid.is_valid():
            self.fail(phone_number_valid.errors)

        location_id = self.data['location_id']
        location = Location.objects.filter(pk=location_id)

        if not location:
            self.fail(dict(invalid_location_id='Please provide a valid country code'))
        
        phone_number = self.data['phone_number']
        otp = self.otp
        if otp is None:
            otp = generate_otp()

        user.artist.location_id = location[0]
        user.artist.save()
        user.otp_code=otp #accesses otp_code attribute
        user.phone_number = self.data['phone_number']
        expiry = timezone.now() + timedelta(minutes=10)
        user.otp_code_expiry = expiry
        user.email_verified = False
        user.save()

        # send otp to email
        email = self.data['email']
        SendOTP.call(email=email, otp=otp) 

        # Send Otp to phone 
        try:
            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            message_to_broadcast = (f'Your Cinch Verification code is {otp}')
            client.messages.create(to=phone_number,
                                from_=settings.TWILIO_NUMBER,
                                body=message_to_broadcast)
            return dict(otp=otp)
        except:
            return self.fail(dict(twilio_error='Having problem connecting to twilio'))

    def get_queryset(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return False
