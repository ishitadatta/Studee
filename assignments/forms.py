from django import forms
from .models import Assignment, AssignmentSubmission
from courses.models import Course
from authentication.models import Account


# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', }),
    )
    deadline = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': "form-control", "type": "date"}))

    class Meta:
        model = Assignment
        fields = ("title", "content", "course", "marks", "deadline")

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'marks': forms.NumberInput(attrs={'class': 'form-control'}),
        }


# ASSIGNMENT SUBMISSION FORM

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model = AssignmentSubmission
        fields = ("file", )

        widgets = {
            'file': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }

