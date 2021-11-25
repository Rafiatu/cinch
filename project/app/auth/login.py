from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from app.action import Action
from lib.lower_strip import strip_and_lower
from db.models.admin import Admin


class Login(Action):
    arguments = ['data']

    def perform(self):
        email = strip_and_lower(self.data.get('email', ''))
        password = self.data.get('password', '')

        if email is None or password is None:
            self.fail(dict(invalid_credential='Please provide both email and password'))
        
        user = authenticate(username=email, password=password)

        if not user:
            self.fail(dict(invalid_credential='Please ensure that your email and password are correct'))

        if not user.email_verified:
            self.fail(dict(verification_failed='Please verify your account'))
            
        token, _ = Token.objects.get_or_create(user=user)
        is_admin = user.is_admin
        if user.is_admin:
            admin_instance = Admin.objects.get(user_id=user.id)
            first_name = admin_instance.first_name
            last_name = admin_instance.last_name
            user_name = user.username
            return dict(token=token.key, first_name=first_name, last_name=last_name, username=user_name, is_admin=is_admin)

        return dict(token=token.key, is_admin=is_admin)
