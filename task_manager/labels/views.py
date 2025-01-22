from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.custom_contrib_mixins import (
    MixinDeleteLabel,
    MixinLoginRequired,
)

from .forms import CreateUpdateLabelForm
from .models import Labels


class LabelsHome(MixinLoginRequired, SuccessMessageMixin, ListView):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = "labels"
    extra_context = {"title": 'Метки'}

    def get_queryset(self):
        return Labels.objects.all()


class LabelsCreate(MixinLoginRequired, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    success_message = 'Метка успешно создана'
    extra_context = {
        "title": 'Создать метку',
        "button_text": 'Создать',
    }


class LabelsUpdate(MixinLoginRequired, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateLabelForm
    model = Labels
    template_name = "actions/create_or_update.html"
    success_url = reverse_lazy("labels")
    pk_url_kwarg = "label_id"
    extra_context = {
        "title": 'Изменение метки',
        "button_text": 'Изменить',
 }
    success_message = 'Метка была успешно изменена'


class LabelsDelete(MixinLoginRequired, SuccessMessageMixin,
                   MixinDeleteLabel, DeleteView):
    model = Labels
    template_name = "actions/delete.html"
    pk_url_kwarg = "label_id"
    context_object_name = "labels_Delete"
    extra_context = {
        "title": 'Удаление метки',
        "button_text": 'Да, удалить',
    }
    success_url = reverse_lazy("labels")
    success_message = "Метка была успешно удалена"
    messages_for_error = ('Невозможно удалить метку, '
                          'потому что она используется')
    redirect_for_error = "labels"