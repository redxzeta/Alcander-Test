from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import Group

# Create your views here.


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='Library Members')
            user.groups.add(group)

        return redirect("/catalog")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})
