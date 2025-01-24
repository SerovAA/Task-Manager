from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.utils.translation import gettext as _

from task_manager.mixins import (DeleteStatusMixin, LoginRequiredMixin)

from .forms import CreateUpdateStatusForm
from .models import Statuses


class StatusesHome(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Statuses
    template_name = 'statuses/statuses.html'
    context_object_name = 'statuses'
    extra_context = {
        'title': _("Statuses")
    }

    def get_queryset(self):
        return Statuses.objects.all()


class StatusesCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    success_message = _("The status has been successfully created")
    extra_context = {
        'title': _("Create a status"),
        'button_text': _("To create"),
    }


class StatusesUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateStatusForm
    model = Statuses
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('statuses')
    pk_url_kwarg = 'status_id'
    success_message = _("Status changed successfully")
    extra_context = {
        'title': _("Status change"),
        'button_text': _("To change"),
    }


class StatusesDelete(LoginRequiredMixin, SuccessMessageMixin,
                     DeleteStatusMixin, DeleteView, ):
    model = Statuses
    template_name = "actions/delete.html"
    success_url = reverse_lazy("statuses")
    success_message = _("Status successfully deleted")
    pk_url_kwarg = "status_id"
    extra_context = {"title": _("Deleting a status")}
    messages_for_error = _(
        "It is not possible to delete the status because it is in use"
    )
    redirect_for_error = "statuses"
