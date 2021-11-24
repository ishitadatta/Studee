from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

app_name = "assignments"

urlpatterns = [
    path('create/(?P<id>\w{0,50})/$', AssignmentCreateView, name='create'),
    path('create/', AssignmentCreateView, name='create'),
    path('', AssignmentView, name='home'),
    url(r'submit/(?P<id>\w{0,50})/$', AssignmentSubmissionView, name='submit'),
    url(r'submit-view/(?P<id>\w{0,50})/$', SubmittedAssignment, name='submit-view'),
    path('submission/(?P<id>\w{0,50})/$', AssignmentSubmissionListView, name='submissions'),
]
