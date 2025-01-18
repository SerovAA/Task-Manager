from django import forms

from .models import Statuses


class CreateUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Имя", "class": "form-control"}
            )
        }