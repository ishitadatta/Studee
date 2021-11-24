from django.urls import path
from django.conf.urls import url
from .views import *

app_name = "forum"

urlpatterns = [
    path("", home, name="home"),
    url(r"detail/(?P<slug>[-\w]+)/$", detail, name="detail"),
    url(r"posts/(?P<slug>[\w-]+)/$", posts, name="posts"),
    path("create_post", create_post, name="create_post"),
    # path("latest_posts", latest_posts, name="latest_posts"),
]
