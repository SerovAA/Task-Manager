from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)
from django_filters.views import FilterView

from task_manager.tasks.filters import FilterTasks

from .forms import CreateUpdateTaskForm
from .models import Tasks


class TaskHome(LoginRequiredMixin, SuccessMessageMixin, FilterView, ListView):
    template_name = 'tasks/tasks.html'
    context_object_name = 'tasks_home'
    filterset_class = FilterTasks
    allow_empty = False
    extra_context = {
        'title': 'Задачи',
        'button_text': 'Показать',
    }

    def get_queryset(self):
        return Tasks.objects.all()


class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    success_message = ('Задача успешно создана')
    extra_context = {
        'title': 'Создать задачу',
        'button_text': 'Создать',
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class TaskShow(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Tasks
    template_name = 'tasks/task.html'
    fields = ['name', 'description', 'status', 'executor']
    context_object_name = 'task_Show'
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Просмотр задачи',
    }


class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CreateUpdateTaskForm
    model = Tasks
    template_name = 'actions/create_or_update.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    extra_context = {
        'title': 'Изменение задачи',
        'button_text': 'Изменить',
    }


class TaskDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Tasks
    template_name = 'actions/delete.html'
    success_url = reverse_lazy('tasks')
    pk_url_kwarg = 'task_id'
    success_message = 'Задача была успешно удалена.'
    messages_for_error = 'Проблема может быть удалена только ее автором.'
    redirect_for_error = "tasks"
    extra_context = {
        'title': 'Удаление задачи'
    }
