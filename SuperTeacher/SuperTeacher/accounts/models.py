from django.contrib.auth.models import AbstractUser
from django.db import models

from SuperTeacher.accounts.validations import validate_file_size


class User(AbstractUser):
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    email = models.EmailField( unique=True)

    username = models.CharField()

    profile_image = models.ImageField(
        upload_to='profile_images/',
        blank=True,
        null=True,
        validators=(validate_file_size,)
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

    USER_TYPE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    user_type = models.CharField(
        max_length=7,
        choices=USER_TYPE_CHOICES
    )



