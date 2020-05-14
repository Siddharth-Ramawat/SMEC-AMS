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
    dept = forms.CharField(max_length=120, required=False)
    registration_number = forms.CharField(max_length=12, required=False)
    job_role = forms.CharField(max_length=100,required=False)
    work_location = forms.CharField(max_length=100, required=False)
    company = forms.CharField(max_length=200, required=False)

    class Meta:
        model = Profile
        fields = ['dept', 'registration_number', 'job_role','work_location','company','image']

    def clean_dept(self):
        return self.cleaned_data['dept'].upper()

    def clean_registration_number(self):
        return self.cleaned_data['registration_number'].upper()

