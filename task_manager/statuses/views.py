from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.custom_contrib_mixins import (
    MixinDeleteStatus,
    MixinLoginRequired,
)

from .forms import CreateUpdateStatusForm
from .models import Statuses


class StatusesHome(MixinLoginRequired, SuccessMessageMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': 'Статусы'
    }

    def get_queryset(self):
        return Statuses.objects.all()


class StatusesCreate(MixinLoginRequired, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    success_message = 'Статус успешно создан'
    extra_context = {
        'title': 'Создать статус',
        'button_text': 'Создать',
    }


class StatusesUpdate(MixinLoginRequired, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    pk_url_kwarg = 'status_id'
    success_message = 'Статус успешно изменен'
    extra_context = {
        'title': 'Изменение статуса',
        'button_text': 'Изменить',
    }


class StatusesDelete(MixinLoginRequired, SuccessMessageMixin,
                      MixinDeleteStatus, DeleteView,):
    model = Statuses
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('statuses')
    denied_url = reverse_lazy('statuses')
    pk_url_kwarg = 'status_id'
    success_message = 'Статус успешно удален'
    extra_context = {
        'title': 'Удаление статуса'
    }
    messages_for_error = ('Невозможно удалить статус, '
                          'потому что он используется')
    redirect_for_error = "statuses"
