from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

from SuperTeacher.accounts.models import TeacherProfile

UserModel = get_user_model()

class Comment(models.Model):
    class Meta:
        indexes = [
            models.Index(fields=['date_time_of_publication']),
        ]
        ordering = ['-date_time_of_publication']

    text = models.TextField(
        max_length=300,
    )

    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)]
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    owner = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    to_teacher = models.ForeignKey(
        to=TeacherProfile,
        on_delete=models.CASCADE,
    )


class Like(models.Model):
    to_teacher = models.ForeignKey(
        to=TeacherProfile,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )
