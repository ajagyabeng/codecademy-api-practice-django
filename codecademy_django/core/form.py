from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name",
                  "username", "passsword1", "password2")