from django import forms
from .models import *
from django.utils.timezone import now


class ClubForm(forms.ModelForm):
    approval_required = forms.BooleanField(required=False)

    class Meta:
        model = Club
        fields = ["name", "description", "approval_required"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


def get_time():
    return now().strftime("%Y-%m-%d %H:%M:%S")


class EventForm(forms.ModelForm):
    date = forms.DateTimeField(initial=get_time)

    class Meta:
        model = Events
        fields = ["name", "description", "location", 'date', 'duration']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }
