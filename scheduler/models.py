from django.db import models
from authentication.models import Account
import os

vaccination = [
    ('Not Vaccinated', 'Not Vaccinated'),
    ('Partially Vaccinated', 'Partially Vaccinated'),
    ('Fully Vaccinated', 'Fully Vaccinated')
]


def get_filename(instance, filename):
    return os.path.join('vaccination', f"{instance.user.username}_{instance.vaccination_status}.{filename.split('.')[-1]}")


class Preference(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE, primary_key=True)
    file = models.FileField(null=True, blank=True, upload_to=get_filename)  
    mode = models.CharField(default='Online', max_length=8, choices=[("Online", "Online"), ("Offline", "Offline")])
    vaccination_status = models.CharField(default='Not Vaccinated', max_length=20, choices=vaccination)
