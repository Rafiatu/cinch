import uuid
from django.db import models
from db.models.artist import Artist


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    artist_id = models.OneToOneField(Artist, on_delete=models.CASCADE)
    bank_code = models.CharField(max_length=20, null=True)
    bank_name = models.CharField(max_length=255, null=True)
    account_name = models.CharField(max_length=255, null=True)
    account_number = models.CharField(max_length=30, null=True, unique=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f"{self.bank_name} {self.bank_code}"
