

class RegisterArtistValidation:
  def validate_artist(data, fail):
        username = data.get('username', '')
        firstname = data.get('first_name', '')
        lastname = data.get('last_name', '')

        # Validate fields
        if firstname and len(firstname) <= 2:
            fail(dict(firstname='firstname must be more than two characters'))
        elif firstname and not firstname.isalpha():
            fail(dict(firstname='firstname must contain only alphabet'))

        if lastname and len(lastname) <= 2:
            fail(dict(lastname='lastname must contain at least two characters'))
        elif lastname and not lastname.isalpha():
            fail(dict(lastname='lastname must contain only alphabet'))

        if username and len(username) <= 2:
            fail(dict(username='username must contain at least 2 characters'))
        return True