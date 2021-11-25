import uuid
from django.db import models
from django.contrib.auth import get_user_model


class Admin(models.Model):
    id              = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id         = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    first_name      = models.CharField(max_length=255)
    last_name       = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name
