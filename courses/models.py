from django.db import models
from authentication.models import Account
import os

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    faculty = models.ForeignKey(Account, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    credits = models.IntegerField(default=4)
    description = models.TextField()

    def __str__(self):
        return self.name


class EnrolledCourse(models.Model):
    id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Account, on_delete=models.CASCADE)

