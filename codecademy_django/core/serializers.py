from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Venue, Photo


class ReadUserSerializer(serializers.ModelSerializer):
    """
    Serializes the User model.
    """
    class Meta:
        model = User
        fields = ("id", "username")
        read_only_fields = fields


class ReadPhotoSerializer(serializers.ModelSerializer):
    """
    Serializes the Photo model for a GET request.
    """
    class Meta:
        model = Photo
        fields = ("id", "venue_name", "image_url", "author", "created")
        read_only_fields = fields


class WritePhotoSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Photo
        fields = ("venue_name", "image_url", "author")

    # def __init__(self, *args, **kwargs):
    #     """
    #     Limits the venues to that of the author only.
    #     """
    #     super().__init__(*args, **kwargs)
    #     author = self.context["request"].user
    #     self.fields["venue_name"].queryset = author.venues.all()


class ReadVenueSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = ReadUserSerializer()
    photo = ReadPhotoSerializer(many=True)

    class Meta:
        model = Venue
        fields = ("id", "name", "address", "created", "author", "photo")
        read_only_fields = fields


class VenueWithPhotoSerializer(serializers.Serializer):
    venue = ReadVenueSerializer()
    photo = ReadPhotoSerializer()


class WriteVenueSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Venue
        fields = ("name", "created", "address", "author")

    # TODO: Figure out how to add photos when adding a venue.
