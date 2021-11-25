from django.db import models


class Location(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    country = models.CharField(max_length=100, unique=True)
    country_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.country} {self.country_code}"
