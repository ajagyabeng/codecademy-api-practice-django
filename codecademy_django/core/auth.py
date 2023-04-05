from django.shortcuts import render, redirect

from .form import MyUserCreationForm


def register_user(request):
    form = MyUserCreationForm()
    context = {"form": form}
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
    return render(request, "accounts/register.html", context)
