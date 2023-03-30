from django.contrib import admin

# Register your models here.
from .models import Venue, Photo

admin.site.register(Venue)
admin.site.register(Photo)
