from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from django.db.models import Prefetch

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Venue, Photo
from .serializers import ReadVenueSerializer, WriteVenueSerializer, ReadPhotoSerializer, WritePhotoSerializer


class PhotoAPIView(ModelViewSet):
    """Handles GET, POST, PUT, PATCH, DELETE requests."""
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    # def get_permissions(self):
    #     """Sets Authentication requirement on some actions"""
    #     if self.action in ("create", "update", "partial_update", "destroy"):
    #         return [IsAuthenticated()]
    #     return [AllowAny()]

    def get_queryset(self):
        """Returns all PHOTO objects belonging to the authenticated user.
        select_related: pre-fetches the foreign key items prior to a query to the Photo model.
        """
        return Photo.objects.select_related("author").filter(author=self.request.user)

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadPhotoSerializer
        return WritePhotoSerializer


class VenueAPIView(ModelViewSet):
    """Handles GET, POST, PUT, PATCH, DELETE requests."""
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Checks for photos and assigns them to the right venues and then return the venues."""
        venues = Venue.objects.prefetch_related(
            Prefetch("photo", queryset=Photo.objects.filter(
                author=self.request.user))
        ).filter(author=self.request.user).order_by("id")

        photo_index = {}

        for photo in Photo.objects.filter(author=self.request.user):
            photo_index.setdefault(photo.venue_name, []).append(photo)

        for venue in venues:
            venue.photo.set(photo_index.get(venue.name, []))

        return venues

    def get_serializer_class(self):
        """Selects the right serialier based on the method type."""
        if self.action in ("list", "retrieve"):
            return ReadVenueSerializer
        return WriteVenueSerializer

# Issue 1: Optimize database operation to reduce LOAD time
