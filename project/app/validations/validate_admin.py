from django.contrib.auth import get_user_model


class RegisterAdminValidation:
  def validate_admin(data, fail):
        email = data.get('email', '')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')

        # Validate fields
        if len(first_name) <= 2 or first_name == '':
            fail(dict(firstname='firstname must be more than two characters'))
        elif first_name and not first_name.isalpha():
            fail(dict(firstname='firstname must contain only alphabet'))
        if len(last_name) <= 2 or last_name == '':
            fail(dict(lastname='lastname must contain at least two characters'))
        elif last_name and not last_name.isalpha():
            fail(dict(lastname='lastname must contain only alphabet'))
        if len(email) <= 2 or email == '':
            fail(dict(username='email must contain at least 2 characters'))
        if get_user_model().objects.filter(email=email).exists():
            fail('A user with this email already exists')
        return True
