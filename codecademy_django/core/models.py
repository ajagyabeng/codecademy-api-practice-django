from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    image_url = models.CharField(max_length=250, null=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="photos")
    created = models.DateTimeField(auto_now_add=True)
    venue = models.ForeignKey(
        "Venue", on_delete=models.CASCADE, null=True, related_name="photos")

    def __str__(self):
        return f"{self.image_url} {self.author.first_name} {self.author.last_name}"


class Venue(models.Model):
    name = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="venues")
    photo = models.ForeignKey(
        Photo, on_delete=models.CASCADE, related_name="venues", default=7)

    def __str__(self):
        return f"{self.name} {self.address}"
