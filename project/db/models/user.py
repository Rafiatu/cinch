import uuid
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField


from .manager import UserManager


class User(AbstractBaseUser):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email           = models.EmailField(max_length=255, unique=True)
    username        = models.CharField(max_length=255, null=True)
    phone_number    = PhoneNumberField(null=True)
    email_verified  = models.BooleanField(default=False)
    otp_code        = models.CharField(max_length=30, null=True)
    otp_code_expiry = models.DateTimeField(default=timezone.now)
    password        = models.CharField(max_length=255)
    is_admin        = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now=False, default=timezone.now)
    updated_at      = models.DateTimeField(auto_now=True)
    objects         = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
