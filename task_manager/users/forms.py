from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
)

HELP_TEXT_1 = ('Обязательное поле. '
               'Не более 150 символов. '
               'Только буквы, цифры и символы @/./+/-/_.')
HELP_TEXT_2 = 'Ваш пароль должен содержать как минимум 3 символа.'
HELP_TEXT_3 = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя',
                               widget=forms.TextInput(
                                   attrs={'class': 'form-control '
                                                   'form-label '
                                                   'container wrapper '
                                                   'flex-grow-1'}))
    password = forms.CharField(label='Пароль',
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    username = forms.CharField(label='Имя пользователя',
                               help_text=HELP_TEXT_1)
    password1 = forms.CharField(label='Пароль',
                                help_text=HELP_TEXT_2)
    password2 = forms.CharField(label='Подтверждение пароля',
                                help_text=HELP_TEXT_3)

    class Meta:
        model = get_user_model()
        fields = [
            'first_name', 'last_name', 'username', 'password1', 'password2']

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже существует")
        return username


class UsersChangeForm(RegisterUserForm):
    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if get_user_model().objects.filter(username=username).exists():
            if username != self.instance.username:
                raise forms.ValidationError("Имя пользователя уже существует")
        return username
