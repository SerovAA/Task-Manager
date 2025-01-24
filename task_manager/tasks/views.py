from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from task_manager.mixins import DeleteTaskMixin, LoginRequiredMixin
from task_manager.tasks.filters import FilterTasks

from .forms import CreateUpdateTaskForm
from .models import Tasks


class TaskHome(LoginRequiredMixin, SuccessMessageMixin,
               FilterView, ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks_home'
    filterset_class = FilterTasks
    allow_empty = False
    extra_context = {
        'title': _('Tasks'),
        'button_text': _('Show'),
    }

    def get_queryset(self):
        return Tasks.objects.all()


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully created')
    extra_context = {
        'title': _('Create a task'),
        'button_text': _('To create'),
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskShow(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Tasks
    template_name = 'tasks/task.html'
    fields = ['name', 'description', 'status', 'executor']
    context_object_name = 'task'
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': _('Viewing a task'),
    }


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    success_message = _('The task has been successfully changed')
    extra_context = {
        "title": _('Changing the task'),
        "button_text": _('To change'),
    }


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin,
                 DeleteTaskMixin, DeleteView):
    model = Tasks
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    success_message = _('The task was successfully deleted')
    extra_context = {
        'title': _('Deleting a task')
    }
    messages_for_error = _('An issue can only be deleted by its author.')
    redirect_for_error = "tasks"