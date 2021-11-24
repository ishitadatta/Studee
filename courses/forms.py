from django import forms
from .models import Course
from authentication.models import Account


# FORM FOR CREATE A COURSE
class CourseCreateForm(forms.ModelForm):
     class Meta:
        model = Course
        fields = ("name", "description", "credits")

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'credits': forms.NumberInput(attrs={'class': 'form-control'}),
        }

