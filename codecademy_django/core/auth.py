from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User

from .form import MyUserCreationForm


def registerUser(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
