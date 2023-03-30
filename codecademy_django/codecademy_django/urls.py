from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from core import views

router = routers.SimpleRouter()
router.register(r'venues', views.VenueAPIView, basename='venue')
router.register(r'photos', views.PhotoAPIView, basename='photo')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', obtain_auth_token, name="obtain_auth_token"),
    path('api/', include(router.urls))
]
