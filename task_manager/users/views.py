from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.custom_contrib_mixins import (
    MixinDeleteUser,
    MixinLoginRequired,
    MixinUpdateUser,
)
from task_manager.users.forms import RegisterUserForm, UsersChangeForm
from task_manager.users.models import User


class Users(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "user"


class Users_Create(SuccessMessageMixin, CreateView):
    form_class = RegisterUserForm
    model = User
    template_name = 'actions/create_or_update.html'
    success_message = ('Пользователь успешно зарегистрирован')
    success_url = reverse_lazy('login')
    extra_context = {
        'title': 'Регистрация',
        'button_text': 'Зарегистрировать',
    }


class Users_Update(MixinLoginRequired, SuccessMessageMixin,
                   MixinUpdateUser, UpdateView):
    form_class = UsersChangeForm
    model = User
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно изменен')
    extra_context = {
        'title': 'Изменение пользователя',
        'button_text': 'Изменить',
    }
    messages_for_error = 'У вас нет прав для изменения другого пользователя.'
    redirect_for_error = 'users'


class User_Delete(MixinLoginRequired, SuccessMessageMixin,
                  MixinDeleteUser, DeleteView):
    model = User
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('users')
    pk_url_kwarg = 'user_id'
    success_message = ('Пользователь успешно удален')
    extra_context = {
        'title': 'Удаление пользователя',
        'button_text': 'Удалить',
    }
    messages_for_error_get = ('Невозможно удалить пользователя, '
                              'потому что он используется')
    messages_for_error_post = ('У вас нет прав для изменения')
    redirect_for_error = 'users'