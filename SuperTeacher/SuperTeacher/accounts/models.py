from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    rating = models.PositiveIntegerField(
        default=0,
    )
