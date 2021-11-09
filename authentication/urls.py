from django.urls import path
from . import views
from .views import *
from .forms import RegistrationForm, AccountAuthenticateForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout


app_name = "authentication"

urlpatterns = [
    path('', views.landingPage, name='landing'),
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
]