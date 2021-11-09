from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class AccountManager(BaseUserManager):
    def create_user(self, username, firstname, lastname, password=None):
        if not username:
            raise ValueError("Users must have an email address")
        if not firstname:
            raise ValueError("Users must have a First Name")

        user = self.model(
            username=self.normalize_email(username),
            email=self.normalize_email(username),
            firstname=firstname,
            lastname=lastname,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, firstname, lastname, password):
        user = self.create_user(
            username=self.normalize_email(username),
            firstname=firstname,
            lastname=lastname,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    username = models.EmailField(
        verbose_name="email", max_length=60, primary_key=True)
    email = models.EmailField(verbose_name="email",
                              max_length=60, null=True, blank=True)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
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

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
