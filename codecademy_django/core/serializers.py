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


class ReadVenueSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = ReadUserSerializer()

    class Meta:
        model = Venue
        fields = ("id", "name", "address", "created", "author")
        read_only_fields = fields


class WriteVenueSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Venue
        fields = ("name", "created", "address", "author")


class ReadPhotoSerializer(serializers.ModelSerializer):
    """
    Serializes the Photo model for a GET request.
    """
    venue = ReadVenueSerializer()

    class Meta:
        model = Photo
        fields = ("id", "image_url", "author", "created", "venue")
        read_only_fields = fields


class WritePhotoSerializer(serializers.ModelSerializer):
    """
    Serializes the Venue model for a POST request.
    """
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    venue = serializers.SlugRelatedField(
        slug_field="name", queryset=Venue.objects.all())

    class Meta:
        model = Photo
        fields = ("venue", "image_url", "author")

    def __init__(self, *args, **kwargs):
        """
        Limits the venues to that of the author only.
        """
        super().__init__(*args, **kwargs)
        author = self.context["request"].user
        self.fields["venue"].queryset = author.venues.all()
