from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_email(self):
        return self.cleaned_data['email'].lower()


class ProfileUpdateForm(forms.ModelForm):
    dept = forms.CharField()
    registration_number = forms.CharField()

    class Meta:
        model = Profile
        fields = ['dept','registration_number','image']

    def clean_registration_number(self):
        return self.cleaned_data['registration_number'].upper()