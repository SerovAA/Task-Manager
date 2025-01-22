from django import forms

from .models import Tasks


class CreateUpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = [
            "name",
            "description",
            "status",
            "executor",
            "labels",
        ]
