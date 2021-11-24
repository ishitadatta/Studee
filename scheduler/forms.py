from django import forms
from .models import Preference


# PREFERENCE FORM
class PreferenceForm(forms.ModelForm):
    mode = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=[("Online", "Online"), ("Offline", "Offline")])
    vaccination_status = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=[
            ('Not Vaccinated', 'Not Vaccinated'),
            ('Partially Vaccinated', 'Partially Vaccinated'),
            ('Fully Vaccinated', 'Fully Vaccinated')
        ],
        required=False
    )

    class Meta:
        model = Preference
        fields = ["mode", "vaccination_status", "file"]

        widgets = {
            'file': forms.FileInput(attrs={'class': 'custom-file-input'}),
        }


