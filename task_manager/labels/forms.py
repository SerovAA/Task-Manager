from django import forms
from django.utils.translation import gettext as _

from .models import Labels


class CreateUpdateLabelForm(forms.ModelForm):
    class Meta:
        model = Labels
        fields = ["name"]
        widgets = {"name": forms.TextInput(
            attrs={"placeholder": _("Name"),
                   "class": "form-control"})
        }