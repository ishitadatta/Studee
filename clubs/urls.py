from django.http import request
from django.urls import path
from django.conf.urls import url
from .views import *

app_name = "clubs"

urlpatterns = [
    path("", home, name="home"),
    url(r"create_event/(?P<slug>[\w-]+)/$", create_event, name="create_event"),
    url(r"(?P<slug>[\w-]+)/$", club_view, name="club"),
    path("create_club", create_club, name="create_club"),
    path("approve_member", approve_member, name="approve_member"),
]

#handler404 = 'main.views.error404'
