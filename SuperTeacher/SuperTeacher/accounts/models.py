from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from SuperTeacher.accounts.managers import AppUserManager
from django.contrib.auth import get_user_model
from django.db import models




class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    is_teacher = models.BooleanField(
        default=False
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['is_teacher',]

    objects = AppUserManager()

UserModel = get_user_model()

class StudentProfile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        blank=True,
        null=True,
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name

        return self.first_name or self.last_name or "Anonymous"


class TeacherProfile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        blank=True,
        null=True,
    )

    TEACHER_TYPE_CHOICES = (
        ('math', 'Mathematics'),
        ('piano', 'Piano'),
        ('music', 'Music'),
        ('english', 'English'),
        ('swimming', 'Swimming'),
        ('billiard', 'Billiard'),
        ('sing', 'Sing'),
        ('boxing', 'Boxing'),
        ('other', 'Other'),
    )

    teacher_type = models.CharField(
        choices=TEACHER_TYPE_CHOICES,
        default='other',
    )

    def get_full_name(self):
        if self.first_name and self.last_name:
            return self.first_name + " " + self.last_name

        return self.first_name or self.last_name or "Anonymous"














