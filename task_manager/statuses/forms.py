from django import forms
from django.utils.translation import gettext as _

from .models import Statuses


class CreateUpdateStatusForm(forms.ModelForm):
    class Meta:
        model = Statuses
        fields = ['name']
        widgets = {
            "name": forms.TextInput(
                attrs={
                    'placeholder': _("Name"),
                    'class': 'form-control'}
            )
        }