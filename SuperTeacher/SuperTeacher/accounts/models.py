from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from SuperTeacher.accounts.managers import AppUserManager
from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone




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

    rating = models.PositiveIntegerField(
        default=0,
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


class Reservation(models.Model):

    class Meta:
        ordering = ['reservation_time']
        unique_together = (
        'student', 'reservation_time')

    student = models.ForeignKey(
        'StudentProfile',
        on_delete=models.CASCADE,
        related_name='student_reservations',
    )

    teacher = models.ForeignKey(
        'TeacherProfile',
        on_delete=models.CASCADE,
        related_name='teacher_reservations',
    )

    reserved_at = models.DateTimeField(
        default=timezone.now,
        help_text="The date and time the reservation is made",
    )

    reservation_time = models.DateTimeField(
        help_text="The date and time the reservation is for",
    )

    status = models.CharField(
        max_length=20,
        choices=(
            ('pending', 'Pending'),
            ('confirmed', 'Confirmed'),
            ('cancelled', 'Cancelled'),
            ('completed', 'Completed'),
        ),
        default='pending',
    )

    notes = models.TextField(
        blank=True,
        null=True,
        help_text="Optional notes or special instructions for the reservation",
    )

    def __str__(self):
        return f"Reservation by {self.student} with {self.teacher} at {self.reservation_time}"












