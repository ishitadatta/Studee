from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class AccountAuthenticateForm(forms.ModelForm):
    username = forms.CharField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'})
    )
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password'})
    )
    class Meta:
        model = Account
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        if not authenticate(username=username, password=password):
            raise forms.ValidationError("Invalid Login")


# REGISTRATION FORM
class RegistrationForm(UserCreationForm):
    # email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password'}))
    type = forms.ChoiceField(
        choices=[("Teacher", "Teacher"), ('Student', 'student')],
        widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ("username", "firstname", "lastname", "password1", "type")

        widgets = {
            'username': forms.EmailInput(attrs={'class': 'form-control'}),
            'firstname': forms.TextInput(attrs={'class': 'form-control'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ("profile_pic", "bio")

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'})
        }
