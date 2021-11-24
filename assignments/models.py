from django.db import models
from authentication.models import Account
from courses.models import Course
from django.utils import timezone
import os


class Assignment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='Teacher')
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    marks = models.IntegerField()
    deadline = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(default=timezone.now)


def get_filename(instance, filename):
    return os.path.join('assignments', f"{instance.user.username}_Assignment{instance.assignment.id}.{filename.split('.')[-1]}")


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    file = models.FileField(null=True, blank=True, upload_to=get_filename)
    marks = models.IntegerField(blank=True, null=True)

