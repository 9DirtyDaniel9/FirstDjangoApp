
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class SignUpForm(UserCreationForm):
    username = forms.CharField(label=_("Введите имя пользователя"), max_length=30, required=False)
    email = forms.EmailField(label=_("Адрес почты"), max_length=254)
    password1 = forms.CharField(label=_("Пароль"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))
    password2 = forms.CharField(label=_("Повторите пароль"), strip=False, widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )