from django.db import models
from authentication.models import Account
from django.utils.text import slugify
from django.utils.timezone import now

# Create your models here.


class Club(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True, primary_key=True)
    description = models.CharField(max_length=400)
    head = models.ForeignKey(Account, on_delete=models.CASCADE)
    founding_date = models.DateTimeField(default=now)
    approval_required = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Club, self).save(*args, **kwargs)


class Members(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    member = models.ForeignKey(Account, on_delete=models.CASCADE)
    approved = models.BooleanField(default=True)
    join_date = models.DateTimeField(default=now)

    class Meta:
        unique_together = ('club', 'member', )


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    location = models.CharField(max_length=100)
    date = models.DateTimeField(default=now)
    duration = models.IntegerField()


class EventAttendees(models.Model):
    event = models.ForeignKey(Events, on_delete=models.CASCADE)
    attendee = models.ForeignKey(Account, on_delete=models.CASCADE)

