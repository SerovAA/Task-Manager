from django.db import models
from django.utils.translation import gettext as _

class Labels(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name=_("Name"))
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name=_("Date of creation"))

    def __str__(self):
        return self.name