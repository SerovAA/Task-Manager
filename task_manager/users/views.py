from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import (
    DeleteUserMixin,
    LoginRequiredMixin,
    UpdateUserMixin,
)
from task_manager.users.forms import RegisterUserForm, UsersChangeForm
from task_manager.users.models import User


class Users(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "user"


class UsersCreate(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = "actions/create_or_update.html"
    success_message = _("The user has been successfully registered")
    success_url = reverse_lazy("login")
    extra_context = {
        "title": _("Registration"),
        "button_text": _("Register"),
    }


class UsersUpdate(LoginRequiredMixin, SuccessMessageMixin,
                  UpdateUserMixin, UpdateView, ):
    form_class = UsersChangeForm
    model = User
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("users")
    pk_url_kwarg = "user_id"
    success_message = _("The user has been successfully changed")
    extra_context = {
        "title": _("Changing the user"),
        "button_text": _("To change"),
    }
    messages_for_error = _("You don't have the rights to change another user.")
    redirect_for_error = "users"


class UserDelete(LoginRequiredMixin, SuccessMessageMixin,
                 DeleteUserMixin, DeleteView, ):
    model = User
    template_name = "actions/delete.html"
    success_url = reverse_lazy("users")
    pk_url_kwarg = "user_id"
    success_message = _("The user has been successfully deleted")
    extra_context = {
        "title": _("Deleting a user"),
        "button_text": _("Remove"),
    }
    flash_get = _("You don't have the rights to change another user.")
    flash_post = _("It is not possible to delete a user because it is in use")
    redirect_for_error = "users"