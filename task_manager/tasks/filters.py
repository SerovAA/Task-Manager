from django.forms import CheckboxInput
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import User


class FilterTasks(FilterSet):
    status = ModelChoiceFilter(
        queryset=Statuses.objects.all()
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all()
    )
    tasks_user = BooleanFilter(
        label = 'Только свои задачи',
        widget = CheckboxInput,
        method = 'filter_tasks_user',
    )

    def filter_tasks_user(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Tasks
        fields = ["status", "executor", "tasks_user"]