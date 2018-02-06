from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model = User
        fields = ('email', 'password')

class SignUpForm(forms.ModelForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:

        model = User
        fields = ('email', 'password')



