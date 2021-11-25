from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_field):

        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superadmin", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_admin", False)
        extra_fields.setdefault("is_superadmin", True)
        extra_fields.setdefault("email_verified", True)
        if extra_fields.get("is_superadmin") is not True:
            raise ValueError('Superadmin must have is_superadmin=True.')

        return self._create_user(email, password, **extra_fields)