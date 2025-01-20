from django.db import models


class Labels(models.Model):
    name = models.CharField(max_length=255, unique=True,
                            verbose_name='Имя')
    time_create = models.DateTimeField(auto_now_add=True,
                                       verbose_name='Дата создания')

    def __str__(self):
        return self.name