from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from catalog.forms import RenewBookForm
from django.contrib.auth.decorators import permission_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

# from django.contrib.auth.get_user_model import user


def viewUsers(request):
    if request.user.is_staff:
        users = User.objects.all()
        return render(request, "viewList.html", {"data": users})
    else:

        return redirect("/catalog/")  # or your url name


class UserListView(generic.ListView):
    """Generic class-based view for a list of books."""

    model = User
    paginate_by = 10
