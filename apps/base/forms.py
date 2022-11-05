from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ("username", "password")
