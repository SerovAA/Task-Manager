from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.utils.translation import gettext as _

from task_manager.mixins import (
    DeleteLabelMixin, LoginRequiredMixin,)

from .forms import CreateUpdateLabelForm
from .models import Labels


class LabelsHome(LoginRequiredMixin, SuccessMessageMixin, ListView):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = "labels"
    extra_context = {"title": _("Labels")}

    def get_queryset(self):
        return Labels.objects.all()


class LabelsCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    success_message = _("The label was created successfully")
    extra_context = {
        "title": _("Create a label"),
        "button_text": _("Create"),
    }


class LabelsUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    pk_url_kwarg = "label_id"
    extra_context = {
        "title": _("Changing the label"),
        "button_text": _("Update"),
    }
    success_message = _("The label has been successfully changed")


class LabelsDelete(LoginRequiredMixin, SuccessMessageMixin,
                   DeleteLabelMixin, DeleteView):
    model = Labels
    template_name = "actions/delete.html"
    pk_url_kwarg = "label_id"
    context_object_name = "labels_Delete"
    success_message = _("The label was successfully deleted")
    extra_context = {
        "title": _("Deleting a label"),
        "button_text": _("Delete"),
    }
    success_url = reverse_lazy("labels")
    messages_for_error = _(
        "It is not possible to remove the label because it is being used")
    redirect_for_error = "labels"