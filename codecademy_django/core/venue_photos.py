from .models import Venue, Photo

from dataclasses import dataclass


@dataclass
class VenueEntry:
    venue: Venue
    photo: Photo


def venue_detail():
    data = []
    query_set = Photo.objects.values("venue").all()

    venue_index = {}

    for venue in Venue.objects.select_related("author"):
        venue_index[venue.pk] = venue

    for photo in query_set:
        venue = venue_index.get(photo["venue"])
        venue_entry = VenueEntry(venue, photo)
        data.append(venue_entry)
        print(data)
    return data
