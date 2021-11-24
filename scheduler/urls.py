from django.urls import path
from .views import *

app_name = "scheduler"

urlpatterns = [
    path('', StudentPreference, name='home'),
] 
         
