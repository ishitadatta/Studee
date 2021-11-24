from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = "courses"

urlpatterns = [
    path('create/(?P<id>\w{0,50})/$', CourseCreateView, name='create'),
    path('create/', CourseCreateView, name='create'),
    path('', CourseView, name='home'),
]
