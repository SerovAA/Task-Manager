from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import CreateUpdateStatusForm
from .models import Statuses


class Statuses_Home(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': 'Статусы'
    }

    def get_queryset(self):
        return Statuses.objects.all()


class Statuses_Create(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    success_message = ('Статус успешно создан')
    extra_context = {
        'title': 'Создать статус',
        'button_text': 'Создать',
    }


class Statuses_Update(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    pk_url_kwarg = 'status_id'
    extra_context = {
        'title': 'Изменение статуса',
        'button_text': 'Изменить',
    }


class Statuses_Delete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Statuses
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('statuses')
    denied_url = reverse_lazy('statuses')
    pk_url_kwarg = 'status_id'
    extra_context = {
        'title': 'Удаление статуса'
    }
