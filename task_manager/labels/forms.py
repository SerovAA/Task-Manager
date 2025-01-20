from django import forms

from .models import Labels


class CreateUpdateLabelForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ["name"]
        widgets = {"name": forms.TextInput(
            attrs={"placeholder": 'Имя',
                   "class": "form-control"})
        }