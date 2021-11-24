from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from tinymce.models import HTMLField
import os


class AccountManager(BaseUserManager):
    def create_user(self, username, firstname, lastname, type='Student', password=None):
        from scheduler.models import Preference

        user = self.model(
            username=self.normalize_email(username),
            email=self.normalize_email(username),
            firstname=firstname,
            lastname=lastname,
            type=type
        )

        user.set_password(password)
        user.save(using=self._db)
        vax = Preference(user=user)
        vax.save()
        return user

    def create_superuser(self, username, firstname, lastname, password):
        user = self.create_user(
            username=self.normalize_email(username),
            firstname=firstname,
            lastname=lastname,
            password=password,
            type='Teacher'
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_filename(instance, filename):
    return os.path.join('authentication/profile_photos', f"{instance.username}.{filename.split('.')[-1]}")


class Account(AbstractBaseUser):
    username = models.EmailField(verbose_name="email", max_length=60, primary_key=True)
    email = models.EmailField(verbose_name="email", max_length=60, null=True, blank=True)
    rn = models.CharField(max_length=10, null=True, blank=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    bio = HTMLField(max_length=100, default='', null=True, blank=True)
    forum_credits = models.FloatField(default=0.0)
    assignment_credits = models.IntegerField(default=0)
    profile_pic = models.ImageField(upload_to=get_filename, default="authentication/profile_photos/default.png")
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    type = models.CharField(default='Student', max_length=8)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    objects = AccountManager()

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    def num_posts(self):
        from forum.models import Post
        return Post.objects.filter(user=self).count()

    def submission_rate(self):
        from assignments.models import Assignment, AssignmentSubmission
        assignments = Assignment.objects.count()
        submissions = AssignmentSubmission.objects.filter(user__username=self.username).values_list('assignment__id', flat=True).distinct().count()
        return int(submissions * 100 / assignments) if assignments != 0 else 0

    def get_clubs(self):
        from clubs.models import Members
        clubs = list(Members.objects.filter(member__username=self.username).values_list('club__slug', flat=True))
        approvals = list(Members.objects.filter(member__username=self.username, approved=False).values_list('club__slug', flat=True))
        return {'clubs': clubs, 'approvals': approvals}

    @property
    def course_credits(self):
        from courses.models import EnrolledCourse
        return sum(list(EnrolledCourse.objects.filter(student__username=self.username).values_list('course__credits', flat=True)))

    @property
    def enrolled_courses(self):
        from courses.models import EnrolledCourse
        return list(EnrolledCourse.objects.filter(student__username=self.username).values_list('course__id', flat=True))

    @property
    def points(self):
        return int(self.forum_credits + self.assignment_credits + self.course_credits + self.club_credits)

    @property
    def tier_points(self):
        return [20, 25, 30, 40, 50, 75, 100, 1000]

    @property
    def tier(self):
        tier = 0
        for i, point in enumerate(self.tier_points):
            if self.points < point:
                tier = i
                break
        return tier

    @property
    def points_to_tier(self):
        points_to_tier = 20
        for i, point in enumerate(self.tier_points):
            if self.points < point:
                points_to_tier = point - self.points
                break
        return points_to_tier

    @property
    def tier_image(self):
        return 'tier_' + str(self.tier) + '.png'

    @property
    def vaccination(self):
        from scheduler.models import Preference
        return Preference.objects.get(user_id=self.username)

    @property
    def club_credits(self):
        from clubs.models import Members, Club
        club = len(list(Members.objects.filter(member__username=self.username).values_list('club__slug', flat=True)))
        head = len(list(Club.objects.filter(head__username=self.username).values_list('slug', flat=True)))
        event = len(self.attended_events) * 0.5
        return club + head + event

    @property
    def club_approvals(self):
        from clubs.models import Members
        return Members.objects.filter(approved=False).all()

    @property
    def attended_events(self):
        from clubs.models import EventAttendees
        return list(EventAttendees.objects.filter(attendee__username=self.username).values_list('event__id', flat=True))

# class Search(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return str(self.name)
