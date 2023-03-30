from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Venue, Photo
from .serializers import ReadVenueSerializer, WriteVenueSerializer, ReadPhotoSerializer, WritePhotoSerializer


class PhotoAPIView(ModelViewSet):
    """Handles GET, POST, PUT, PATCH, DELETE requests."""
    # permission_classes = [IsAuthenticated]
    lookup_field = "pk"

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        """Returns all PHOTO objects belonging to the authenticated user.
        select_related: pre-fetches the foreign key items prior to a query to the Photo model.
        """
        # return Photo.objects.select_related("venue", "author").filter(author=self.request.user)
        return Photo.objects.select_related("venue", "author")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadPhotoSerializer
        return WritePhotoSerializer


class VenueAPIView(ModelViewSet):
    """Handles GET, POST, PUT, PATCH, DELETE requests."""

    def get_permissions(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return [IsAuthenticated()]
        return [AllowAny()]

    def get_queryset(self):
        return Venue.objects.select_related("author")

    def get_serializer_class(self):
        if self.action in ("list", "retrieve"):
            return ReadVenueSerializer
        return WriteVenueSerializer
