from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext as _

from task_manager.labels.models import Labels
from task_manager.statuses.models import Statuses
from task_manager.users.models import User


class Tasks(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_('Name')
    )
    time_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Date of creation')
    )
    description = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_('Description'),
    )
    status = models.ForeignKey(
        Statuses,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_("Status"),
        related_name='status',
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.PROTECT,
        null=True,
        related_name='author',
        verbose_name=_('Author'),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        null=True,
        verbose_name=_('Executor'),
        related_name='executor',
    )
    labels = models.ManyToManyField(
        Labels,
        blank=True,
        verbose_name=_('Labels'),
        related_name='labels',
    )

    def __str__(self):
        return self.name