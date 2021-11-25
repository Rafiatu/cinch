import uuid
from django.db import models
from django.contrib.auth import get_user_model
from db.models.location import Location


class Artist(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30, null=True)
    lastname = models.CharField(max_length=30, null=True)
    avatar_url = models.URLField(max_length=255,
                                 default='http://res.cloudinary.com/cinchapi/image/upload/v1605789407/re1ouirm2sujfwz5afgx.png',
                                 null=True)
    number_of_songs = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    location_id = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f" {self.firstname} {self.lastname}"
