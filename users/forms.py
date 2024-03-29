from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # It gives us a nested namespace for configurations and keeps the config
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        # It gives us a nested namespace for configurations and keeps the config
        model = User
        fields = ['username', 'email']


class ProfilUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']