from django.urls import path
from . import views
from .views import *


app_name = "authentication"

urlpatterns = [
    path('home/', views.homePage, name='home'),
    path('', views.landingPage, name='landing'),
    path('register/', views.register, name='register'),
    path('accounts/login/', views.loginView, name='login'),
    path('profile/', views.profile, name='profile'),
    path('editProfile/', views.editProfile, name='editProfile'),
    path('logout/', views.logout_view, name='logout'),
    path('deleteuser/', views.deleteuser, name='deleteuser')
]
