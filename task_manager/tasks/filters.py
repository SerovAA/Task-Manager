from django.forms import CheckboxInput
from django.utils.translation import gettext as _
from django_filters import BooleanFilter, FilterSet, ModelChoiceFilter

from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.tasks.models import Tasks
from task_manager.users.models import User


class FilterTasks(FilterSet):
    status = ModelChoiceFilter(
        queryset=Statuses.objects.all(),
        label=_("Status")
    )
    executor = ModelChoiceFilter(
        queryset=User.objects.all(),
        label=_("Executor")
    )
    labels = ModelChoiceFilter(
        queryset=Labels.objects.all(),
        label=_("Label")
    )
    tasks_user = BooleanFilter(
        label=_("Only your own tasks"),
        widget=CheckboxInput,
        method='filter_tasks_user'
    )

    def filter_tasks_user(self, queryset, name, value):
        if value:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset

    class Meta:
        model = Tasks
        fields = ["status", "executor", "labels", "tasks_user"]