from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext as _

TEXT = _("Required field. No more than 150 characters. ")
TEXT2 = _("Only letters, numbers and symbols @/./+/-/_.")


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label=_("Name"))
    last_name = forms.CharField(label=_("Family"))
    username = forms.CharField(
        label = _('Username'),
        help_text=TEXT + TEXT2)
    password1 = forms.CharField(
        label = _('Password'),
        widget = forms.PasswordInput())
    password2 = forms.CharField(
        label = _('Password confirmation'),
        widget = forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username",
            "password1",
            "password2",
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError(_('The username already exists'))
        return username


class UsersChangeForm(RegisterUserForm):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "username"
        ]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            if username != self.instance.username:
                raise forms.ValidationError(_('The username already exists'))
        return username
