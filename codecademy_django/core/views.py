from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

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
        """Checks for photos and assigns them to the right venues"""
        return Venue.objects.select_related("author").filter(author=self.request.user)

    def get_serializer_class(self):
        """Selects the right serialier based on the method type."""
        if self.action in ("list", "retrieve"):
            return ReadVenueSerializer
        return WriteVenueSerializer

    def list(self, request):
        """Lists all venues. Checks the """
        venues = self.get_queryset()
        photos = Photo.objects.select_related("author").filter(
            author=self.request.user)

        for venue in venues:
            for photo in photos:
                if photo.venue_name == venue.name:
                    venue.photo.add(photo)

        serializer_class = self.get_serializer_class()
        serializer = serializer_class(venues, many=True)
        return Response(serializer.data)

# Issue 1: Optimize database operation to reduce LOAD time
# Issue 2: Execute first part of part of list method on a general basis so retrieve could also do add phot in it is null.
