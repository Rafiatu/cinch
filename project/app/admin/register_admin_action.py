from app.action import Action
from django.contrib.auth import get_user_model
from db.models.admin import Admin
from django.db import transaction
from lib.lower_strip import strip_and_lower
from lib.admin_pwd import generate_password
from app.emails.email_template import email_template
from ..validations.validate_admin import RegisterAdminValidation


class RegisterAdmin(Action):
    arguments = ['data']

    @transaction.atomic
    def perform(self):
        # Get all the Data
        email=strip_and_lower(self.data.get('email', ''))
        first_name=self.data.get('first_name', '')
        last_name=self.data.get('last_name', '')
        username = (first_name + last_name)
        password = generate_password()
        email_subject = 'Cinch Admin Details'

        #validate data
        valid_admin = RegisterAdminValidation.validate_admin(self.data, self.fail)
        if not valid_admin: return valid_admin

        #create user instance and save
        user = get_user_model().objects.create(
            email=email,
            username = username,
            password = password,
            email_verified=True,
            is_admin=True
        )
        user.set_password(password)

        #create admin instance and save
        admin = Admin.objects.create(
            user_id = user,
            first_name=first_name,
            last_name=last_name,
        )

        #save user to db
        user.save()

        #save admin to the db
        admin.save()

        email_body = f'''
            Hello {first_name}, Welcome to Cinch, we are delighted to have you on board.
            <br><br><b>Note: <i>Here are your admin details.</i> </b>
            <br><br>Email:<strong>{email}</strong> 
            <br><br>Password:<strong>{password}</strong> 
            <br><br><b>Note: <i>Kindly change your password once you sign in.</i> </b>'''

        email_template(email_subject, email, email_body)

        success_data = dict(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        return success_data
